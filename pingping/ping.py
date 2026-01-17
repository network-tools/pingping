import logging
import os
import re
import subprocess
import sys

from shconfparser.parser import Parser


class Ping:
    p = Parser()
    ping_data = {}
    data = ""
    name = "pingping"

    def __init__(
        self, command="ping", count=4, layer=3, timeout=3, log_level=logging.INFO, log_format=None
    ):
        self.os = os.name
        self.command = [command]
        self.command = self._set_ping(count, layer=layer, timeout=timeout)
        self.format = log_format
        self.logger = self.set_logger_level(log_level)

    def set_logger_level(self, log_level):
        if self.format is None:
            self.format = "[ %(levelname)s ] :: [ %(name)s ] :: %(message)s"
        logging.basicConfig(stream=sys.stdout, level=log_level, format=self.format, datefmt=None)
        logger = logging.getLogger(self.name)
        logger.setLevel(log_level)
        return logger

    def _set_ping(self, count, layer, timeout):
        if layer != 3:
            self.command.append(f"-c {count}")
            self.command.append(f"-t {timeout}")
            return self.command
        if self.os == "nt":
            self.command.append(f"-n {count}")
        elif self.os == "posix":
            self.command.append(f"-c {count}")
        return self.command

    @classmethod
    def is_valid_ip(cls, ip):
        m = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", str(ip).strip())
        return bool(m) and all(0 <= int(n) <= 255 for n in m.groups())

    def _add_ip(self, ip):
        if self.is_valid_ip(ip):
            return self.command + [ip]

    def ping(self, ip):
        command = self._add_ip(ip)
        # print(command)
        if command:
            p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            # print(out.decode())
            out = out.decode().split("\n")
            return self.fetch_ping_data(out, command=command[0])
        else:
            logging.error(f"invalid ip entered {ip}")

    @classmethod
    def _fetch_ip(cls):
        pattern = r"^.*?(\d+\.\d+\.\d+\.\d+)(?: |]|:|\[).*"
        result = cls.p.search.search_in_tree(pattern, cls.data)
        if result:
            cls.ping_data["ip"] = result.group(result.lastindex)

    @classmethod
    def _fetch_loss_percentage(cls, command):
        pattern = r".*(?: +|\()(\d+\.?\d*?)%.*"
        result = cls.p.search.search_in_tree(pattern, cls.data)
        if result:
            if command == "tcping":
                cls.ping_data["loss_percentage"] = 100 - float(result.group(result.lastindex))
            else:
                cls.ping_data["loss_percentage"] = float(result.group(result.lastindex))

    @classmethod
    def _fetch_packets_count(cls):
        pattern = r"^\s*.*?:.*(\d+), .*, .*%.*"
        result = cls.p.search.search_in_tree(pattern, cls.data)
        if result:
            cls.ping_data["packets_transmitted"] = int(result.group(result.lastindex))
            return

        pattern = r"^\s*(\d+).*%.*"
        result = cls.p.search.search_in_tree(pattern, cls.data)
        if result:
            cls.ping_data["packets_transmitted"] = int(result.group(result.lastindex))
            return

    @classmethod
    def _fetch_time(cls):
        pattern = r".* *= *([0-9\.]+)\s*\/\s*([0-9\.]+)\s*\/\s*([0-9\.]+).*"
        result = cls.p.search.search_in_tree(pattern, cls.data)
        if cls._set_time(result):
            return

        pattern = (
            r".*?= *(\d+(?:\.\d+)?).*?,.*?= *(\d+(?:\.\d+)?).*?,.*= *(\d+(?:\.\d+)?)\s*\S+\s*$"
        )
        result = cls.p.search.search_in_tree(pattern, cls.data)
        if cls._set_time(result, index=[1, 3, 2]):
            return

    @classmethod
    def _set_time(cls, result, index=None):
        if index is None:
            index = [1, 2, 3]
        if result:
            cls.ping_data["min"] = float(result.group(index[0]))
            cls.ping_data["avg"] = float(result.group(index[1]))
            cls.ping_data["max"] = float(result.group(index[2]))
            cls.ping_data["time_in"] = "ms"
            return True

    @classmethod
    def fetch_ping_data(cls, data, command="ping", loss_percentage_filter=75):
        if type(data) is not list:
            data = str(data).split("\n")  # .encode('utf-8') issue in 2.7

        # print(data)
        cls.ping_data = {}
        cls.data = cls.p.parse_data(data)
        cls._fetch_ip()
        cls._fetch_loss_percentage(command)
        cls._fetch_packets_count()

        if cls.ping_data.get("loss_percentage", 0) <= loss_percentage_filter:
            cls._fetch_time()
        return cls.ping_data


def get_index(given_list, element):
    try:
        return given_list.index(element)
    except ValueError:
        return None


def run():
    obj = None
    result = None
    ip_address = None
    if len(sys.argv) >= 2:
        _help = ["-h", "--help"]
        _proxy = ["-l4", "--web", "--tcp", "--http"]
        _count = ["-c", "--count"]

        for each in sys.argv[1:]:
            if Ping.is_valid_ip(each):
                ip_address = each
                break

        if ip_address is None:
            for each in _help:
                if get_index(sys.argv, each):
                    help()

        for each in _proxy:
            if get_index(sys.argv, each):
                os.environ["LC_CTYPE"] = "en_US.UTF-8"
                obj = Ping(command="tcping", layer=4, timeout=3)

        for each in _count:
            index = get_index(sys.argv, each)
            if index:
                count = int(sys.argv[index + 1])
                obj = Ping(count=count)

        if obj is None:
            obj = Ping()

        result = obj.ping(ip_address)
        return result
    else:
        help()


def help():
    print("Usage pingping  <ip-address>")
    print("                -c | --count <Number>")
    print("                -l4 | --web | --tcp | --http (ping over proxy)")
    print("                -h | --help")
    exit(-1)


if __name__ == "__main__":
    obj = Ping()
    print(obj.ping("192.168.1.1"))
    print(obj.ping("127.0.0.1"))
    print(obj.ping("1.1.1.1"))
    obj = Ping(count=4)
    print(obj.ping("8.8.8.8"))
    obj = Ping(command="tcping", layer=4, timeout=3)
    print(obj.ping("8.8.8.8"))
    print(obj.ping("192.168.1.1"))

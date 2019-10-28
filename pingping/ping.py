import os
import re
import sys
import subprocess
import logging
from shconfparser.parser import Parser


class Ping:
    command = ['ping']
    p = Parser()
    ping_data = {}
    data = ''
    name = 'pingping'

    def __init__(self, count=4, log_level=logging.INFO, log_format=None):
        self.os = os.name
        self.command = self._set_ping(count)
        self.format = log_format
        self.logger = self.set_logger_level(log_level)

    def set_logger_level(self, log_level):
        if self.format is None:
            self.format = '[ %(levelname)s ] :: [ %(name)s ] :: %(message)s'
        logging.basicConfig(stream=sys.stdout, level=log_level, format=self.format, datefmt=None)
        logger = logging.getLogger(self.name)
        logger.setLevel(log_level)
        return logger

    def _set_ping(self, count):
        if self.os == 'nt':
            self.command.append('-n {}'.format(count))
        elif self.os == 'posix':
            self.command.append('-c {}'.format(count))
        return self.command

    def is_valid_ip(self, ip):
        m = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", str(ip).strip())
        return bool(m) and all(map(lambda n: 0 <= int(n) <= 255, m.groups()))

    def _add_ip(self, ip):
        if self.is_valid_ip(ip):
            return self.command + [ip]

    def ping(self, ip):
        command = self._add_ip(ip)
        if command:
            p = subprocess.Popen(command, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            out, err = p.communicate()
            # print(out.decode())
            out = out.decode().split('\n')
            return self.fetch_ping_data(out)
        else:
            logging.error('invalid ip entered {}'.format(ip))

    @classmethod
    def _fetch_ip(cls):
        pattern = r'^.*?(\d+\.\d+\.\d+\.\d+)(?: |]|:).*'
        result = cls.p.search.search_in_tree(pattern, cls.data)
        if result:
            cls.ping_data['ip'] = result.group(result.lastindex)

    @classmethod
    def _fetch_loss_percentage(cls):
        pattern = r'.*(?: +|\()(\d+\.?\d*?)%.*'
        result = cls.p.search.search_in_tree(pattern, cls.data)
        if result:
            cls.ping_data['loss_percentage'] = float(result.group(result.lastindex))

    @classmethod
    def _fetch_time(cls):
        pattern = r'.* *= *([0-9\.]+)\s*\/\s*([0-9\.]+)\s*\/\s*([0-9\.]+).*'
        result = cls.p.search.search_in_tree(pattern, cls.data)
        if cls._set_time(result):
            return

        pattern = r'.*?= *(\d+).*?,.*?= *(\d+).*?,.*= *(\d+)\s*\S+\s*$'
        result = cls.p.search.search_in_tree(pattern, cls.data)
        if cls._set_time(result, index=[1, 3, 2]):
            return

    @classmethod
    def _set_time(cls, result, index=[1, 2, 3]):
        if result:
            cls.ping_data['min'] = float(result.group(index[0]))
            cls.ping_data['avg'] = float(result.group(index[1]))
            cls.ping_data['max'] = float(result.group(index[2]))
            cls.ping_data['time_in'] = 'ms'
            return True

    @classmethod
    def fetch_ping_data(cls, data, loss_percentage_filter=75):
        if type(data) is not list:
            data = str(data).split('\n') # .encode('utf-8') issue in 2.7

        # print(data)
        cls.ping_data = {}
        cls.data = cls.p.parse_data(data)
        cls._fetch_ip()
        cls._fetch_loss_percentage()

        if cls.ping_data.get('loss_percentage', 0) <= loss_percentage_filter:
            cls._fetch_time()
        return cls.ping_data


def run():
    obj = Ping()
    if len(sys.argv) >= 2:
        print(obj.ping(sys.argv[1]))
    else:
        print("Expecting an argument.")
        print("e.g.: pingping <ip-address>")


if __name__ == "__main__":
    obj = Ping()
    print(obj.ping('192.168.1.1'))
    print(obj.ping('127.0.0.1'))
    print(obj.ping('1.1.1.1'))


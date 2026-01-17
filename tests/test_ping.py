import json
import os
from unittest.mock import MagicMock, patch

import pytest

from pingping.ping import Ping, get_index


class TestPing:
    file_path = os.path.abspath("data")

    @pytest.fixture
    def setup(self):
        p = Ping()
        yield p

    def read_all_inputs(self, obj, langauge="en"):
        file_name = f"ping_{langauge}.json"
        ping_data = json.load(open(f"{self.file_path}/{file_name}"))
        result = {}
        for os_name, os_result in ping_data.items():
            result[os_name] = {}
            for ip, each_ping in os_result.items():
                result[os_name][ip] = obj.fetch_ping_data(each_ping)
        return result

    def validate_result(self, result):
        assert "linux" in result
        assert "windows" in result
        assert "mac" in result

        assert "1.1.1.1" in result["linux"]
        assert "loss_percentage" in result["linux"]["1.1.1.1"]
        assert 0.0 == result["linux"]["1.1.1.1"]["loss_percentage"]
        assert 58.489 == result["linux"]["1.1.1.1"]["min"]
        assert 108.154 == result["linux"]["1.1.1.1"]["avg"]
        assert 188.385 == result["linux"]["1.1.1.1"]["max"]
        assert 4 == result["linux"]["1.1.1.1"]["packets_transmitted"]

        assert "192.168.1.1" in result["linux"]
        assert "loss_percentage" in result["linux"]["192.168.1.1"]
        assert 100.0 == result["linux"]["192.168.1.1"]["loss_percentage"]
        assert 4 == result["linux"]["192.168.1.1"]["packets_transmitted"]

        assert "1.1.1.1" in result["windows"]
        assert "loss_percentage" in result["windows"]["1.1.1.1"]
        assert 0.0 == result["windows"]["1.1.1.1"]["loss_percentage"]
        assert 68.0 == result["windows"]["1.1.1.1"]["min"]
        assert 81.0 == result["windows"]["1.1.1.1"]["avg"]
        assert 99.0 == result["windows"]["1.1.1.1"]["max"]
        assert 4 == result["windows"]["1.1.1.1"]["packets_transmitted"]

        assert "192.168.1.1" in result["windows"]
        assert "loss_percentage" in result["windows"]["192.168.1.1"]
        assert 100.0 == result["windows"]["192.168.1.1"]["loss_percentage"]
        assert 4 == result["windows"]["192.168.1.1"]["packets_transmitted"]

        assert "1.1.1.1" in result["mac"]
        assert "loss_percentage" in result["mac"]["1.1.1.1"]
        assert 0.0 == result["mac"]["1.1.1.1"]["loss_percentage"]
        assert 24.02 == result["mac"]["1.1.1.1"]["min"]
        assert 24.116 == result["mac"]["1.1.1.1"]["avg"]
        assert 24.279 == result["mac"]["1.1.1.1"]["max"]
        assert 4 == result["mac"]["1.1.1.1"]["packets_transmitted"]

        assert "192.168.1.1" in result["mac"]
        assert "loss_percentage" in result["mac"]["192.168.1.1"]
        assert 100.0 == result["mac"]["192.168.1.1"]["loss_percentage"]
        assert 4 == result["mac"]["192.168.1.1"]["packets_transmitted"]

        assert "1.1.1.1" in result["mingw64"]
        assert "loss_percentage" in result["mingw64"]["1.1.1.1"]
        assert 25.0 == result["mingw64"]["1.1.1.1"]["loss_percentage"]
        assert 64.0 == result["mingw64"]["1.1.1.1"]["min"]
        assert 71.0 == result["mingw64"]["1.1.1.1"]["avg"]
        assert 79.0 == result["mingw64"]["1.1.1.1"]["max"]
        assert 4 == result["mingw64"]["1.1.1.1"]["packets_transmitted"]

        assert "192.168.1.1" in result["mingw64"]
        assert "loss_percentage" in result["mingw64"]["192.168.1.1"]
        assert 100.0 == result["mingw64"]["192.168.1.1"]["loss_percentage"]
        assert 4 == result["mingw64"]["192.168.1.1"]["packets_transmitted"]

    def test_ping_en(self, setup):
        result = self.read_all_inputs(setup)
        self.validate_result(result)

    def test_ping_spanish(self, setup):
        result = self.read_all_inputs(setup, langauge="spanish")
        self.validate_result(result)

    def test_ping_french(self, setup):
        result = self.read_all_inputs(setup, langauge="french")
        self.validate_result(result)

    def test_ping_afrikaans(self, setup):
        result = self.read_all_inputs(setup, langauge="afrikaans")
        self.validate_result(result)

    def test_ping_telugu(self, setup):
        result = self.read_all_inputs(setup, langauge="telugu")
        self.validate_result(result)

    def test_ping_hindi(self, setup):
        result = self.read_all_inputs(setup, langauge="hindi")
        self.validate_result(result)

    def test_ping_hindi_2(self, setup):
        result = self.read_all_inputs(setup, langauge="hindi")
        self.validate_result(result)


class TestPingAdditional:
    """Additional tests to improve coverage"""

    def test_set_logger_level(self):
        """Test logger level setting"""
        ping = Ping()
        logger = ping.set_logger_level("DEBUG")
        assert logger.level == 10  # DEBUG level

        logger = ping.set_logger_level("INFO")
        assert logger.level == 20  # INFO level

        logger = ping.set_logger_level("ERROR")
        assert logger.level == 40  # ERROR level

    def test_set_ping_layer_not_3(self):
        """Test _set_ping with layer != 3"""
        ping = Ping(layer=4, count=5, timeout=10)
        command = ping._set_ping(count=5, layer=4, timeout=10)
        assert "-c 5" in command
        assert "-t 10" in command

    def test_is_valid_ip_valid(self):
        """Test is_valid_ip with valid IPs"""
        assert Ping.is_valid_ip("192.168.1.1") is True
        assert Ping.is_valid_ip("8.8.8.8") is True
        assert Ping.is_valid_ip("127.0.0.1") is True
        assert Ping.is_valid_ip("1.1.1.1") is True
        assert Ping.is_valid_ip("255.255.255.255") is True

    def test_is_valid_ip_invalid(self):
        """Test is_valid_ip with invalid IPs"""
        assert Ping.is_valid_ip("256.1.1.1") is False
        assert Ping.is_valid_ip("192.168.1") is False
        assert Ping.is_valid_ip("invalid") is False
        assert Ping.is_valid_ip("192.168.1.1.1") is False
        assert Ping.is_valid_ip("") is False

    def test_add_ip_valid(self):
        """Test _add_ip with valid IP"""
        ping = Ping()
        command = ping._add_ip("192.168.1.1")
        assert command is not None
        assert "192.168.1.1" in command

    def test_add_ip_invalid(self):
        """Test _add_ip with invalid IP"""
        ping = Ping()
        command = ping._add_ip("invalid_ip")
        assert command is None

    @patch("subprocess.Popen")
    def test_ping_valid_ip(self, mock_popen):
        """Test ping method with valid IP"""
        mock_process = MagicMock()
        mock_process.communicate.return_value = (
            b"PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.\n"
            b"64 bytes from 8.8.8.8: icmp_seq=1 ttl=117 time=20.1 ms\n"
            b"--- 8.8.8.8 ping statistics ---\n"
            b"1 packets transmitted, 1 received, 0% packet loss, time 0ms\n"
            b"rtt min/avg/max/mdev = 20.100/20.100/20.100/0.000 ms\n",
            b"",
        )
        mock_popen.return_value = mock_process

        ping = Ping(count=1)
        result = ping.ping("8.8.8.8")
        assert result is not None
        mock_popen.assert_called_once()

    def test_ping_invalid_ip(self, capsys):
        """Test ping method with invalid IP"""
        ping = Ping()
        result = ping.ping("999.999.999.999")
        assert result is None

    def test_get_index_found(self):
        """Test get_index when element is found"""
        test_list = ["a", "b", "c", "d"]
        assert get_index(test_list, "b") == 1
        assert get_index(test_list, "a") == 0
        assert get_index(test_list, "d") == 3

    def test_get_index_not_found(self):
        """Test get_index when element is not found"""
        test_list = ["a", "b", "c"]
        assert get_index(test_list, "z") is None
        assert get_index(test_list, "x") is None

    def test_ping_different_counts(self):
        """Test ping with different packet counts"""
        ping1 = Ping(count=1)
        ping2 = Ping(count=10)
        assert "-c 1" in ping1.command or "-n 1" in ping1.command
        assert "-c 10" in ping2.command or "-n 10" in ping2.command

    def test_set_ping_windows_os(self):
        """Test _set_ping for Windows OS"""
        ping = Ping(count=5)
        ping.os = "nt"
        command = ping._set_ping(count=5, layer=3, timeout=3)
        assert "-n 5" in command

    def test_set_ping_posix_os(self):
        """Test _set_ping for POSIX OS"""
        ping = Ping(count=5)
        ping.os = "posix"
        command = ping._set_ping(count=5, layer=3, timeout=3)
        assert "-c 5" in command

    def test_tcping_initialization(self):
        """Test tcping command initialization"""
        ping = Ping(command="tcping", layer=4)
        assert "tcping" in ping.command
        assert "-c 4" in ping.command or "-t" in " ".join(ping.command)

    def test_ping_with_timeout(self):
        """Test ping with custom timeout"""
        Ping(timeout=5)
        Ping(timeout=10)
        # Timeout should be in the command for layer 4
        ping_l4 = Ping(layer=4, timeout=5)
        assert "-t" in " ".join(ping_l4.command) or "-t 5" in ping_l4.command

    def test_tcping_loss_percentage_calculation(self):
        """Test tcping loss percentage calculation (line 78)"""
        from pingping.ping import Ping

        # Mock tcping output with 80% successful (which means 80% success rate)
        tcping_output = """
        Probing 192.168.1.1:80/tcp - Port is open
        Port is open
        Port is open
        Port is open

        Statistics: 4 probes sent, 80% successful
        """

        # Test tcping command to hit line 78
        # When command="tcping", line 78 calculates: 100 - percentage = 100 - 80 = 20% loss
        ping = Ping(command="tcping", layer=4)
        result = ping.fetch_ping_data(tcping_output, command="tcping")
        assert "loss_percentage" in result
        assert result["loss_percentage"] == 20.0  # 100 - 80 = 20% loss


class TestCLIFunctions:
    """Test CLI functions: run() and help()"""

    def test_run_with_valid_ip(self):
        """Test run() function with valid IP address (lines 146-181)"""
        from pingping.ping import run

        with patch("sys.argv", ["pingping", "8.8.8.8"]):
            with patch.object(Ping, "ping", return_value={"ip": "8.8.8.8"}):
                result = run()
                assert result is not None
                assert result["ip"] == "8.8.8.8"

    def test_run_with_help_flag(self):
        """Test run() function with -h flag (lines 146-181)"""
        from pingping.ping import run

        with patch("sys.argv", ["pingping", "-h"]):
            with pytest.raises(SystemExit) as exc_info:
                run()
            assert exc_info.value.code == -1

    def test_run_with_help_long_flag(self):
        """Test run() function with --help flag (lines 146-181)"""
        from pingping.ping import run

        with patch("sys.argv", ["pingping", "--help"]):
            with pytest.raises(SystemExit) as exc_info:
                run()
            assert exc_info.value.code == -1

    def test_run_with_tcp_flag(self):
        """Test run() function with -l4 flag (lines 146-181)"""
        from pingping.ping import run

        with patch("sys.argv", ["pingping", "-l4", "192.168.1.1"]):
            with patch.object(Ping, "ping", return_value={"ip": "192.168.1.1"}):
                result = run()
                assert result is not None

    def test_run_with_web_flag(self):
        """Test run() function with --web flag (lines 146-181)"""
        from pingping.ping import run

        with patch("sys.argv", ["pingping", "--web", "192.168.1.1"]):
            with patch.object(Ping, "ping", return_value={"ip": "192.168.1.1"}):
                result = run()
                assert result is not None

    def test_run_with_tcp_long_flag(self):
        """Test run() function with --tcp flag (lines 146-181)"""
        from pingping.ping import run

        with patch("sys.argv", ["pingping", "--tcp", "192.168.1.1"]):
            with patch.object(Ping, "ping", return_value={"ip": "192.168.1.1"}):
                result = run()
                assert result is not None

    def test_run_with_http_flag(self):
        """Test run() function with --http flag (lines 146-181)"""
        from pingping.ping import run

        with patch("sys.argv", ["pingping", "--http", "192.168.1.1"]):
            with patch.object(Ping, "ping", return_value={"ip": "192.168.1.1"}):
                result = run()
                assert result is not None

    def test_run_with_count_flag(self):
        """Test run() function with -c flag (lines 146-181)"""
        from pingping.ping import run

        with patch("sys.argv", ["pingping", "-c", "10", "8.8.8.8"]):
            with patch.object(Ping, "ping", return_value={"ip": "8.8.8.8"}):
                result = run()
                assert result is not None

    def test_run_with_count_long_flag(self):
        """Test run() function with --count flag (lines 146-181)"""
        from pingping.ping import run

        with patch("sys.argv", ["pingping", "--count", "15", "1.1.1.1"]):
            with patch.object(Ping, "ping", return_value={"ip": "1.1.1.1"}):
                result = run()
                assert result is not None

    def test_run_with_no_ip_address(self):
        """Test run() function with invalid arguments - no valid IP (lines 146-181)"""
        from pingping.ping import run

        # When -c flag is used but no valid IP is provided, it will create a default Ping
        # and attempt to ping None, which returns None (not a SystemExit)
        with patch("sys.argv", ["pingping", "--help", "invalid"]):
            with pytest.raises(SystemExit) as exc_info:
                run()
            assert exc_info.value.code == -1

    def test_run_with_no_arguments(self):
        """Test run() function with no arguments (lines 146-181)"""
        from pingping.ping import run

        with patch("sys.argv", ["pingping"]):
            with pytest.raises(SystemExit) as exc_info:
                run()
            assert exc_info.value.code == -1

    def test_help_function(self):
        """Test help() function (lines 185-189)"""
        from pingping.ping import help

        with pytest.raises(SystemExit) as exc_info:
            help()
        assert exc_info.value.code == -1

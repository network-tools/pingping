import pytest
import os
import sys
import json

from pingping.ping import Ping


class TestPing:
    file_path = os.path.abspath('data')

    @pytest.fixture
    def setup(self):
        if sys.version_info.major == 2:
            import imp
            imp.reload(sys)
            sys.setdefaultencoding('utf-8')

        p = Ping()
        yield p

    def read_all_inputs(self, obj, langauge='en'):
        file_name = 'ping_{}.json'.format(langauge)
        ping_data = json.load(open('{}/{}'.format(self.file_path, file_name)))
        result = {}
        for os, os_result in ping_data.items():
            result[os] = {}
            for ip, each_ping in os_result.items():
                result[os][ip] = obj.fetch_ping_data(each_ping)
        return result

    def validate_result(self, result):
        assert 'linux' in result
        assert 'windows' in result
        assert 'mac' in result

        assert '1.1.1.1' in result['linux']
        assert 'loss_percentage' in result['linux']['1.1.1.1']
        assert 0.0 == result['linux']['1.1.1.1']['loss_percentage']
        assert 58.489 == result['linux']['1.1.1.1']['min']
        assert 108.154 == result['linux']['1.1.1.1']['avg']
        assert 188.385 == result['linux']['1.1.1.1']['max']
        assert 4 == result['linux']['1.1.1.1']['packets_transmitted']

        assert '192.168.1.1' in result['linux']
        assert 'loss_percentage' in result['linux']['192.168.1.1']
        assert 100.0 == result['linux']['192.168.1.1']['loss_percentage']
        assert 4 == result['linux']['192.168.1.1']['packets_transmitted']

        assert '1.1.1.1' in result['windows']
        assert 'loss_percentage' in result['windows']['1.1.1.1']
        assert 0.0 == result['windows']['1.1.1.1']['loss_percentage']
        assert 68.0 == result['windows']['1.1.1.1']['min']
        assert 81.0 == result['windows']['1.1.1.1']['avg']
        assert 99.0 == result['windows']['1.1.1.1']['max']
        assert 4 == result['windows']['1.1.1.1']['packets_transmitted']

        assert '192.168.1.1' in result['windows']
        assert 'loss_percentage' in result['windows']['192.168.1.1']
        assert 100.0 == result['windows']['192.168.1.1']['loss_percentage']
        assert 4 == result['windows']['192.168.1.1']['packets_transmitted']

        assert '1.1.1.1' in result['mac']
        assert 'loss_percentage' in result['mac']['1.1.1.1']
        assert 0.0 == result['mac']['1.1.1.1']['loss_percentage']
        assert 24.02 == result['mac']['1.1.1.1']['min']
        assert 24.116 == result['mac']['1.1.1.1']['avg']
        assert 24.279 == result['mac']['1.1.1.1']['max']
        assert 4 == result['mac']['1.1.1.1']['packets_transmitted']

        assert '192.168.1.1' in result['mac']
        assert 'loss_percentage' in result['mac']['192.168.1.1']
        assert 100.0 == result['mac']['192.168.1.1']['loss_percentage']
        assert 4 == result['mac']['192.168.1.1']['packets_transmitted']

        assert '1.1.1.1' in result['mingw64']
        assert 'loss_percentage' in result['mingw64']['1.1.1.1']
        assert 25.0 == result['mingw64']['1.1.1.1']['loss_percentage']
        assert 64.0 == result['mingw64']['1.1.1.1']['min']
        assert 71.0 == result['mingw64']['1.1.1.1']['avg']
        assert 79.0 == result['mingw64']['1.1.1.1']['max']
        assert 4 == result['mingw64']['1.1.1.1']['packets_transmitted']

        assert '192.168.1.1' in result['mingw64']
        assert 'loss_percentage' in result['mingw64']['192.168.1.1']
        assert 100.0 == result['mingw64']['192.168.1.1']['loss_percentage']
        assert 4 == result['mingw64']['192.168.1.1']['packets_transmitted']

    def test_ping_en(self, setup):
        result = self.read_all_inputs(setup)
        self.validate_result(result)

    def test_ping_spanish(self, setup):
        result = self.read_all_inputs(setup, langauge='spanish')
        self.validate_result(result)

    def test_ping_french(self, setup):
        result = self.read_all_inputs(setup, langauge='french')
        self.validate_result(result)

    def test_ping_afrikaans(self, setup):
        result = self.read_all_inputs(setup, langauge='afrikaans')
        self.validate_result(result)

    def test_ping_telugu(self, setup):
        result = self.read_all_inputs(setup, langauge='telugu')
        self.validate_result(result)

    def test_ping_hindi(self, setup):
        result = self.read_all_inputs(setup, langauge='hindi')
        self.validate_result(result)

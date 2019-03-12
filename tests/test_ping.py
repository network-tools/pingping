import pytest
import os
import json

from pingping.ping import Ping


class TestPing:
    file_path = os.path.abspath('data')

    @pytest.fixture
    def setup(self):
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

        assert '192.168.1.1' in result['linux']
        assert 'loss_percentage' in result['linux']['192.168.1.1']
        assert 100.0 == result['linux']['192.168.1.1']['loss_percentage']

        assert '1.1.1.1' in result['windows']
        assert 'loss_percentage' in result['windows']['1.1.1.1']
        assert 0.0 == result['windows']['1.1.1.1']['loss_percentage']
        assert 68.0 == result['windows']['1.1.1.1']['min']
        assert 81.0 == result['windows']['1.1.1.1']['avg']
        assert 99.0 == result['windows']['1.1.1.1']['max']

        assert '192.168.1.1' in result['windows']
        assert 'loss_percentage' in result['windows']['192.168.1.1']
        assert 100.0 == result['windows']['192.168.1.1']['loss_percentage']

        assert '1.1.1.1' in result['mac']
        assert 'loss_percentage' in result['mac']['1.1.1.1']
        assert 0.0 == result['mac']['1.1.1.1']['loss_percentage']
        assert 24.02 == result['mac']['1.1.1.1']['min']
        assert 24.116 == result['mac']['1.1.1.1']['avg']
        assert 24.279 == result['mac']['1.1.1.1']['max']

        assert '192.168.1.1' in result['mac']
        assert 'loss_percentage' in result['mac']['192.168.1.1']
        assert 100.0 == result['mac']['192.168.1.1']['loss_percentage']

        assert '1.1.1.1' in result['mingw64']
        assert 'loss_percentage' in result['mingw64']['1.1.1.1']
        assert 25.0 == result['mingw64']['1.1.1.1']['loss_percentage']
        assert 64.0 == result['mingw64']['1.1.1.1']['min']
        assert 71.0 == result['mingw64']['1.1.1.1']['avg']
        assert 79.0 == result['mingw64']['1.1.1.1']['max']

        assert '192.168.1.1' in result['mingw64']
        assert 'loss_percentage' in result['mingw64']['192.168.1.1']
        assert 100.0 == result['mingw64']['192.168.1.1']['loss_percentage']

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

#
# def test_ping_arabic():
#     result = """[pinging ask-leo.com [50.28.23.175] مع 32 بايت من البيانات:
# الرد من 50.28.23.175: bytes = 32 time = 69ms TTL = 47
#   الرد من 50.28.23.175: bytes = 32 time = 70ms TTL = 47
#   الرد من 50.28.23.175: bytes = 32 time = 69ms TTL = 47
#   الرد من 50.28.23.175: bytes = 32 time = 69ms TTL = 47
# إحصائيات Ping عن 50.28.23.175:
#   الحزم: المرسلة = 4 ، المستلمة = 4 ، فقدت = 0 (خسارة 0٪) ،
#   أوقات تقريبًا ذهابًا وإيابًا بالمللي ثانية:
#   الحد الأدنى = 69 مللي ثانية والحد الأقصى = 70 مللي ثانية والمتوسط = 69 مللي ثانية
# """
#
#
# def test_ping_malayalam():
#     result = """32 ബൈറ്റുകളുടെ വിവരമുള്ള പിംഗ് ചെയ്യൽ ask-leo.com [50.28.23.175]:
# 50.28.23.175: ബൈറ്റുകൾ = 32 സമയം = 69ms ടിടിഎൽ = 47 ൽ നിന്നുമുള്ള മറുപടി
#   50.28.23.175: ബൈറ്റുകൾ = 32 ടൈം = 70ms ടിടിഎൽ = 47 ൽ നിന്നുമുള്ള മറുപടി
#   50.28.23.175: ബൈറ്റുകൾ = 32 സമയം = 69ms ടിടിഎൽ = 47 ൽ നിന്നുമുള്ള മറുപടി
#   50.28.23.175: ബൈറ്റുകൾ = 32 സമയം = 69ms ടിടിഎൽ = 47 ൽ നിന്നുമുള്ള മറുപടി
# 50.28.23.175 എന്നതിനായുള്ള പിംഗ് സ്ഥിതിവിവരം:
#   പാക്കറ്റുകൾ: അയച്ചത് = 4, സ്വീകരിച്ചു = 4, നഷ്ടമായ = 0 (0% നഷ്ടം),
#   മില്ലി-സെക്കൻഡിൽ ഏകദേശം അന്തിമ സഞ്ചാര യാത്രകൾ
#   കുറഞ്ഞത് = 69, പരമാവധി = 70, ശരാശരി = 69 മി
# """
#
#
# def test_ping_telugu():
#     result = """డేటాను 32 బైట్లు కలిగి ఉన్న pinging ask-leo.com [50.28.23.175]:
# 50.28.23.175: బైట్లు = 32 టైమ్ = 69ms TTL = 47 నుండి ప్రత్యుత్తరం
#   50.28.23.175: బైట్లు = 32 టైమ్ = 70ms TTL = 47 నుండి ప్రత్యుత్తరం
#   50.28.23.175: బైట్లు = 32 టైమ్ = 69ms TTL = 47 నుండి ప్రత్యుత్తరం
#   50.28.23.175: బైట్లు = 32 టైమ్ = 69ms TTL = 47 నుండి ప్రత్యుత్తరం
# 50.28.23.175 కోసం పింగ్ గణాంకాలు:
#   ప్యాకెట్లు: పంపబడింది = 4, స్వీకరించారు = 4, లాస్ట్ = 0 (0% నష్టం),
#   మిల్లీ సెకన్లలో సరాసరి రౌండ్ ట్రిప్ టైమ్స్:
#   కనీస = 69ms, గరిష్ఠ = 70ms, సగటు = 69ms
# """
#
#
# def test_ping_korean():
#     result = """ask-leo.com [50.28.23.175]에 32 바이트의 데이터로 핑 (pingping)
# 50.28.23.175에서 응답 : 바이트 = 32 시간 = 69ms TTL = 47
#   50.28.23.175에서 응답 : 바이트 = 32 시간 = 70ms TTL = 47
#   50.28.23.175에서 응답 : 바이트 = 32 시간 = 69ms TTL = 47
#   50.28.23.175에서 응답 : 바이트 = 32 시간 = 69ms TTL = 47
# 50.28.23.175에 대한 Ping 통계 :
#   패킷 : 보낸 = 4,받은 = 4, 분실 = 0 (0 % 손실),
#   대략 왕복 시간 (밀리 초) :
#   최소 = 69ms, 최대 = 70ms, 평균 = 69ms
# """
#
#
# def test_ping_chinese():
#     result = """使用32字节数据pinging ask-leo.com [50.28.23.175]：
# 来自50.28.23.175的回复：bytes = 32 time = 69ms TTL = 47
#   来自50.28.23.175的回复：bytes = 32 time = 70ms TTL = 47
#   来自50.28.23.175的回复：bytes = 32 time = 69ms TTL = 47
#   来自50.28.23.175的回复：bytes = 32 time = 69ms TTL = 47
# Ping统计数据为50.28.23.175：
#   数据包：已发送= 4，已接收= 4，已丢失= 0（0％丢失），
#   以毫秒为单位的近似往返时间：
#   最小值= 69ms，最大值= 70ms，平均值= 69ms
# """
#

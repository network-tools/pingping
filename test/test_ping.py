from pingping.ping import Ping
import pytest
import os
import json


class TestPingPing:
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

    def test_ping_en(self, setup):
        result = self.read_all_inputs(setup)

        assert 'linux' in result
        assert 'windows' in result
        assert 'mac' in result

        assert '1.1.1.1' in result['linux']
        print(result)


# def test_ping_en():
#     result = """Pinging ask-leo.com [50.28.23.175] with 32 bytes of data:
# Reply from 50.28.23.175: bytes=32 time=69ms TTL=47
# Reply from 50.28.23.175: bytes=32 time=70ms TTL=47
# Reply from 50.28.23.175: bytes=32 time=69ms TTL=47
# Reply from 50.28.23.175: bytes=32 time=69ms TTL=47
# Ping statistics for 50.28.23.175:
# Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
# Approximate round trip times in milli-seconds:
# Minimum = 69ms, Maximum = 70ms, Average = 69ms
# """
#     print(result)
#
#
# # Need to remove after testing.
# def test_ping_french():
#     result = """Envoyez une requête à ask-leo.com [50.28.23.175] avec 32 octets de données:
# Réponse de 50.28.23.175: octets = 32 fois = 69ms TTL = 47
#   Réponse du 50.28.23.175: octets = 32 fois = 70ms TTL = 47
#   Réponse de 50.28.23.175: octets = 32 fois = 69ms TTL = 47
#   Réponse de 50.28.23.175: octets = 32 fois = 69ms TTL = 47
# Statistiques de Ping pour 50.28.23.175:
#   Paquets: envoyés = 4, reçus = 4, perdus = 0 (0% de perte),
#   Durée approximative du trajet aller et retour en millisecondes:
#   Minimum = 69 ms, Maximum = 70 ms, Moyenne = 69 ms
# """
#
#
# def test_ping_spanish():
#     result = """Pinging ask-leo.com [50.28.23.175] con 32 bytes de datos:
# Respuesta de 50.28.23.175: bytes = 32 tiempo = 69ms TTL = 47
#   Respuesta de 50.28.23.175: bytes = 32 tiempo = 70 ms TTL = 47
#   Respuesta de 50.28.23.175: bytes = 32 tiempo = 69ms TTL = 47
#   Respuesta de 50.28.23.175: bytes = 32 tiempo = 69ms TTL = 47
# Estadísticas de pingping para 50.28.23.175:
#   Paquetes: Enviados = 4, Recibidos = 4, Perdidos = 0 (0% de pérdida),
#   Tiempo aproximado de ida y vuelta en milisegundos:
#   Mínimo = 69 ms, Máximo = 70 ms, promedio = 69 ms
# """
#
#
# def test_ping_afrikaans():
#     result = """Pinging ask-leo.com [50.28.23.175] met 32 grepe data:
# Antwoord van 50.28.23.175: bytes = 32 tyd = 69ms TTL = 47
#   Antwoord van 50.28.23.175: bytes = 32 tyd = 70ms TTL = 47
#   Antwoord van 50.28.23.175: bytes = 32 tyd = 69ms TTL = 47
#   Antwoord van 50.28.23.175: bytes = 32 tyd = 69ms TTL = 47
# Ping statistieke vir 50.28.23.175:
#   Pakkette: Gestuur = 4, Ontvang = 4, Verlore = 0 (0% verlies),
#   Geskatte rondreis tye in milli sekondes:
#   Minimum = 69ms, Maksimum = 70ms, Gemiddelde = 69ms
# """
#
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

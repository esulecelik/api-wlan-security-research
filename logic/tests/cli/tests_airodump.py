from django.test import TestCase,SimpleTestCase
from ...cli.airodump import AirodumpScanner

class TestAirodump(SimpleTestCase):
   
    def setUp(self):
        
        # self.output_example ="""
        # BSSID              PWR  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH ESSID
        # 00:14:6C:7A:41:88  -43      125      678   10   6  54e  WPA2 CCMP   PSK  HomeNetwork
        # 00:25:9C:CF:1C:AC  -78       45       22    0  11  54e  WEP  WEP    SK   OldRouter
        # 88:36:6C:22:1B:9F  -55      200     1056   14   1  54e  WPA2 CCMP   PSK  CafeWiFi

        # BSSID              STATION            PWR   Rate    Lost  Frames  Probe
        # 00:14:6C:7A:41:88  40:16:7E:19:2D:11  -40   54e-54e     0     450
        # 00:14:6C:7A:41:88  38:20:56:9A:3B:4C  -42   24e-54e     3     120
        # 88:36:6C:22:1B:9F  74:DA:38:9E:12:1F  -50   18e-24e     0     320
        # """
        
    def test_sniff(self):
        scanner = AirodumpScanner._sniff("wlan0")
        print(f"{scanner}")
        self.assertIsInstance(scanner, list)
    
    
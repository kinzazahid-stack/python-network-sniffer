import unittest
from scapy.layers.inet import IP, TCP

from src.parser import parse_packet


class TestParser(unittest.TestCase):

    def test_tcp_packet(self):
        packet = IP(src="192.168.1.1", dst="192.168.1.2") / TCP(sport=1234, dport=80)

        info = parse_packet(packet)

        self.assertEqual(info["Protocol"], "TCP")
        self.assertEqual(info["Source"], "192.168.1.1")
        self.assertEqual(info["Destination"], "192.168.1.2")


if __name__ == "__main__":
    unittest.main()
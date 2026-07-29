from scapy.all import sniff
from parser import parse_packet


def process_packet(packet):
    info = parse_packet(packet)

    if info:
        print(
            f"{info['Source']} --> {info['Destination']} | "
            f"{info['Protocol']} | "
            f"{info['Length']} Bytes"
        )


def start_sniffer():
    print("Starting Network Sniffer...\n")
    sniff(prn=process_packet, store=False)
from scapy.all import IP, TCP, UDP


def parse_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        length = len(packet)

        src_port = "-"
        dst_port = "-"

        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            protocol = "TCP"

        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            protocol = "UDP"

        return {
            "Source": src_ip,
            "Destination": dst_ip,
            "Protocol": protocol,
            "Length": length,
            "Source Port": src_port,
            "Destination Port": dst_port,
        }

    return None
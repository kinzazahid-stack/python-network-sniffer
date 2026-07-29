from scapy.layers.inet import IP, TCP, UDP, ICMP


def parse_packet(packet):
    """
    Extract useful information from a network packet.

    Returns:
        dict: Parsed packet information
        None: If packet doesn't contain an IP layer
    """

    if IP not in packet:
        return None

    info = {
        "Source": packet[IP].src,
        "Destination": packet[IP].dst,
        "Protocol": "Unknown",
        "Length": len(packet),
        "Source Port": "-",
        "Destination Port": "-"
    }

    # TCP Packet
    if TCP in packet:
        info["Protocol"] = "TCP"
        info["Source Port"] = packet[TCP].sport
        info["Destination Port"] = packet[TCP].dport

    # UDP Packet
    elif UDP in packet:
        info["Protocol"] = "UDP"
        info["Source Port"] = packet[UDP].sport
        info["Destination Port"] = packet[UDP].dport

    # ICMP Packet
    elif ICMP in packet:
        info["Protocol"] = "ICMP"

    else:
        protocol_number = packet[IP].proto
        info["Protocol"] = f"IP ({protocol_number})"

    return info
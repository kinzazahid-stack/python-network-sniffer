"""
Packet filtering utilities.
"""

from scapy.layers.inet import TCP, UDP, ICMP


def match_protocol(packet, protocol):
    """
    Check if packet matches the selected protocol.

    Args:
        packet: Scapy packet
        protocol (str): tcp, udp, icmp or None

    Returns:
        bool
    """

    if protocol is None:
        return True

    protocol = protocol.lower()

    if protocol == "tcp":
        return TCP in packet

    if protocol == "udp":
        return UDP in packet

    if protocol == "icmp":
        return ICMP in packet

    return False
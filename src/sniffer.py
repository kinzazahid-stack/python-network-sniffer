from scapy.all import sniff

from parser import parse_packet
from analyzer import TrafficAnalyzer
from filters import match_protocol
from utils import print_packet, save_to_csv

# Global analyzer instance
analyzer = TrafficAnalyzer()


def process_packet(packet, protocol=None, save=False):
    """
    Process each captured packet.
    """

    # Apply protocol filter
    if not match_protocol(packet, protocol):
        return

    # Parse packet
    info = parse_packet(packet)

    if info:
        # Update statistics
        analyzer.update(info)

        # Display packet
        print_packet(info)

        # Save packet if requested
        if save:
            save_to_csv(info)


def start_sniffer(packet_count=0, protocol=None, save=False):
    """
    Start live network packet capture.

    Args:
        packet_count (int): Number of packets to capture.
                            0 = Unlimited
        protocol (str): tcp, udp, icmp or None
        save (bool): Save packet details to CSV
    """

    print("\n" + "=" * 60)
    print("Starting Network Sniffer...")
    print("Press CTRL + C to stop.")
    print("=" * 60 + "\n")

    try:
        sniff(
            prn=lambda pkt: process_packet(pkt, protocol, save),
            count=packet_count,
            store=False,
        )

    except KeyboardInterrupt:
        print("\nCapture stopped by user.")

    except PermissionError:
        print("\nPermission denied!")
        print("Run this program as Administrator/root.")
        print("Live packet capture is not supported in GitHub Codespaces.")

    except Exception as e:
        print(f"\nUnexpected Error: {e}")

    finally:
        analyzer.print_summary()
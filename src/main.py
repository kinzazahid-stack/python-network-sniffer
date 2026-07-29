import argparse

from sniffer import start_sniffer
from utils import print_banner


def main():
    """Main entry point of the application."""

    parser = argparse.ArgumentParser(
        description="Python Network Sniffer"
    )

    parser.add_argument(
        "--count",
        type=int,
        default=0,
        help="Number of packets to capture (0 = unlimited)"
    )

    parser.add_argument(
        "--protocol",
        type=str,
        default=None,
        choices=["tcp", "udp", "icmp"],
        help="Capture only a specific protocol"
    )

    parser.add_argument(
        "--save",
        action="store_true",
        help="Save captured packets to CSV"
    )

    args = parser.parse_args()

    print_banner()

    start_sniffer(
        packet_count=args.count,
        protocol=args.protocol,
        save=args.save
    )


if __name__ == "__main__":
    main()
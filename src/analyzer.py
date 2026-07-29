from collections import Counter


class TrafficAnalyzer:
    """
    Analyze captured network traffic.
    """

    def __init__(self):
        self.total_packets = 0
        self.protocols = Counter()
        self.source_ips = Counter()
        self.destination_ips = Counter()
        self.packet_sizes = []

    def update(self, packet_info):
        """
        Update statistics using parsed packet information.
        """

        if packet_info is None:
            return

        self.total_packets += 1

        self.protocols[packet_info["Protocol"]] += 1
        self.source_ips[packet_info["Source"]] += 1
        self.destination_ips[packet_info["Destination"]] += 1
        self.packet_sizes.append(packet_info["Length"])

    def average_packet_size(self):
        if not self.packet_sizes:
            return 0

        return sum(self.packet_sizes) / len(self.packet_sizes)

    def print_summary(self):
        """
        Print traffic statistics.
        """

        print("\n" + "=" * 60)
        print("NETWORK TRAFFIC SUMMARY")
        print("=" * 60)

        print(f"Total Packets : {self.total_packets}")

        print("\nProtocol Distribution")

        if self.protocols:
            for protocol, count in self.protocols.items():
                print(f"  {protocol:<10} : {count}")

        print("\nTop Source IPs")

        for ip, count in self.source_ips.most_common(5):
            print(f"  {ip:<18} {count}")

        print("\nTop Destination IPs")

        for ip, count in self.destination_ips.most_common(5):
            print(f"  {ip:<18} {count}")

        print(f"\nAverage Packet Size : {self.average_packet_size():.2f} Bytes")

        print("=" * 60)
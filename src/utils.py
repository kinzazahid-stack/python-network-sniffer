import csv
import os
from datetime import datetime
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)


def print_banner():
    """Display application banner."""
    print(Fore.CYAN + "=" * 60)
    print(Fore.GREEN + "        Python Network Sniffer")
    print(Fore.YELLOW + "   Capture and Analyze Network Traffic")
    print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)


def print_packet(info):
    """Print packet information in a readable format."""
    print(
        f"{Fore.GREEN}[{info['Protocol']}] "
        f"{Fore.WHITE}{info['Source']}:{info['Source Port']} "
        f"{Fore.YELLOW}--> "
        f"{Fore.WHITE}{info['Destination']}:{info['Destination Port']} "
        f"{Fore.CYAN}({info['Length']} Bytes)"
    )


def save_to_csv(packet_data, filename="data/captures/capture.csv"):
    """
    Save captured packet information to a CSV file.
    """

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    file_exists = os.path.isfile(filename)

    with open(filename, "a", newline="") as csvfile:
        fieldnames = [
            "Timestamp",
            "Source",
            "Destination",
            "Protocol",
            "Length",
            "Source Port",
            "Destination Port",
        ]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        packet_data["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow(packet_data)

    print(Fore.BLUE + f"Packet saved to {filename}")
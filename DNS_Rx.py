from scapy.all import *
import os

DNS_Destination = {
    "8.8.8.8": "0",
    "8.8.4.4": "1",
    "76.76.2.0": "2",
    "76.76.10.0": "3",
    "9.9.9.9": "4",
    "149.112.112.112": "5",
    "208.67.222.222": "6",
    "208.67.220.220": "7",
    "1.1.1.1": "8",
    "1.0.0.1": "9",
    "94.140.14.14": "10",
    "94.140.15.15": "11",
    "185.228.168.9": "12",
    "185.228.169.9": "13",
    "76.76.19.19": "14",
    "76.223.122.150": "15"
}

DNS_qname = {
    "youtube.com.": "0",
    "www.google.com.": "1",
    "www.blogger.com.": "2",
    "linkedin.com.": "3",
    "cloudflare.com.": "4",
    "microsoft.com.": "5",
    "apple.com.": "6",
    "support.google.com.": "7"
}

pcapName = input("Enter the name of the pcap file: ")
srcIP = input("Enter the source IP: ")

packets = PcapReader(pcapName)

binary_message = ""
dns_info = []
for packet in packets:
    if packet.haslayer(IP):
        if packet.haslayer(DNS):
            if packet[IP].src == srcIP:
                if packet[DNS].qr == 0:
                    destination = packet[IP].dst
                    qname = packet[DNS].qd.qname.decode('utf-8')
                    if destination in DNS_Destination and qname in DNS_qname:
                        dns_binary = "0" + bin(int(DNS_qname[qname]))[2:].zfill(3)  # Convert DNS value to binary
                        ip_binary = bin(int(DNS_Destination[destination]))[2:].zfill(4)  # Convert IP value to binary
                        combined_binary = dns_binary + ip_binary
                        print(combined_binary)
                        binary_message += combined_binary
                        dns_info.append((destination, qname))
for data in dns_info:
    print(data)
# Convert binary message to ASCII characters
message = ""
for i in range(0, len(binary_message), 8):
    byte = binary_message[i:i+8]
    message += chr(int(byte, 2))

print("Hidden message:", message)

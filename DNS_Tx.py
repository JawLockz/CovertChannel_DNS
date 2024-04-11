from scapy.all import *
import os
import requests
import time
import random

DNS_Destination = {
    "0": "8.8.8.8",
    "1": "8.8.4.4",
    "2": "76.76.2.0",
    "3": "76.76.10.0",
    "4": "9.9.9.9",
    "5": "149.112.112.112",
    "6": "208.67.222.222",
    "7": "208.67.220.220",
    "8": "1.1.1.1",
    "9": "1.0.0.1",
    "10": "94.140.14.14",
    "11": "94.140.15.15",
    "12": "185.228.168.9",
    "13": "185.228.169.9",
    "14": "76.76.19.19",
    "15": "76.223.122.150"
}

DNS_qname = {
    "0": "youtube.com",
    "1": "www.google.com",
    "2": "www.blogger.com",
    "3": "linkedin.com",
    "4": "cloudflare.com",
    "5": "microsoft.com",
    "6": "apple.com",
    "7": "support.google.com"
}

def send_dns_query(domain_name, dns_server):
    # Create DNS query packet
    dns_query_packet = IP(dst=dns_server)/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=domain_name, qtype='A'))

    # Send DNS query packet and receive response
    dns_response = sr1(dns_query_packet, verbose=0)

    # Process DNS response
    if dns_response and dns_response.haslayer(DNS):
        for i in range(dns_response[DNS].ancount):
            print("IPv4 Address:", dns_response[DNSRR][i].rdata)
    else:
        print("No response received or invalid response.")

#Function to check if the given message is ascii to ensure it can be transmitted using this method
def is_ascii(s):
    return all(ord(c) < 128 for c in s)
  
def toBinary(a):
  ascii_nums,binary=[],[]
  for i in a:
    ascii_nums.append(ord(i))
  for i in ascii_nums:
    binary.append(int(bin(i)[2:]))
  return binary

def short_sleep():
    sleep_duration = random.uniform(1, 5)
    time.sleep(sleep_duration)

if os.getuid() != 0:
    print("This script needs to be run as root to work")
    exit(1)

ascii = False
while not(ascii):
    message = input("Enter your text to send:")
    ascii = is_ascii(message)
    if not (ascii):
        print("Given string contains non-ascii characters, try again.")

# Hint to use this as a forensics exercise by referencing the two sources for our dictionaries in our network traffic
try:
    r = requests.get("http://www.lifewire.com/free-and-public-dns-servers-2626062", timeout=5)
    print(r.status_code)
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print("Error:", e)
short_sleep()
try:
    r = requests.get("http://moz.com/top-500/download/?table=top500Domains", timeout=5)
    print(r.status_code)
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print("Error:", e)

binary = toBinary(message)
print(binary)
for char in binary:
    short_sleep()
    domain_name = str(char)[:3]  # Domain name to query
    dns_server = str(char)[3:7]  # DNS server IP address
    domain_name = DNS_qname[str(int(domain_name, 2))]
    dns_server = DNS_Destination[str(int(dns_server, 2))]
    send_dns_query(domain_name, dns_server)
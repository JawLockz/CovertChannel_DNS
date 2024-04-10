from scapy.all import *
import os
import math

DNS_Destination = {
    "8.8.8.8":"0",
    "8.8.4.4":"1",
    "76.76.2.0":"2",
    "76.76.10.0":"3",
    "9.9.9.9":"4",
    "149.112.112.112":"5",
    "208.67.222.222":"6",
    "208.67.220.220":"7",
    "1.1.1.1":"8",
    "1.0.0.1":"9",
    "94.140.14.14":"10",
    "94.140.15.15":"11",
    "185.228.168.9":"12",
    "185.228.169.9":"13",
    "76.76.19.19":"14",
    "76.223.122.150":"15"
}

DNS_qname = {
    "youtube.com":"0",
    "www.google.com":"1",
    "www.blogger.com":"2",
    "linkedin.com":"3",
    "cloudflare.com":"4",
    "microsoft.com":"5",
    "apple.com":"6",
    "support.google.com":"7"    
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

if os.getuid() != 0:
    print("This script needs to be run as root to work")
    exit(1)

ascii = False
while not(ascii):
    message = input("Enter your text to send:")
    ascii = is_ascii(message)
    if not (ascii):
        print("Given string contains non-ascii characters, try again.")



domain_name = "netflix.com"  # Domain name to query
dns_server = "8.8.8.8"  # DNS server IP address
send_dns_query(domain_name, dns_server)
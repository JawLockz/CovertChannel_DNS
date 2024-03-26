from scapy.all import *
import os

if os.getuid() != 0:
    print("This script needs to be run as root to work")
    exit(1)

# if interface not in scapy.interfaces.get_if_list():
#     print("Warning, interface not found in interface list")

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

domain_name = "netflix.com"  # Domain name to query
dns_server = "8.8.8.8"  # DNS server IP address
send_dns_query(domain_name, dns_server)
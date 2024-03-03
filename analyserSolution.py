from scapy import *
from scapy.layers.inet import IP, TCP, ICMP
import random

def generate(num_Packets): # Start nested function
    packets = [] # Create list to append packets at the end

    def clean_Packet(): # Create clean packet with random IP adresses
        src_ip = ".".join(str(random.randint(0, 255)) for _ in range(4)) 
        dst_ip = ".".join(str(random.randint(0, 255)) for _ in range(4)) 

        packet = IP(src=src_ip, dst=dst_ip) / TCP(dport=random.randint(1, 65535))
        return packet
    
    def malicious_Packet(): # Create simulated malicious packet
        src_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        dst_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))

        if random.random() < 0.5: #If probability less than 50%, simulate port scanning
            dport = random.randint(1, 65535)
            packet = IP(src=src_ip, dst=dst_ip) / TCP(dport=dport, flags="S")
        else: # Else, generate ICMP packet with custom payload indicating suspicious activity
            packet = IP(src=src_ip, dst=dst_ip) / ICMP() / "Suspicious activity"

        return packet
    
    clean_packets = [clean_Packet() for _ in range(num_packets // 2)] # Generates half 'num_packets' of clean packets
    malicious_packets = [malicious_Packet() for _ in range(num_packets // 2)] # Generates half 'num_packets' of malicious packets
    
    # Appends clean and malicious packets in 'packets' list
    packets.extend(clean_packets)
    packets.extend(malicious_packets)

    return packets


# Generate set number of packets
num_packets = 200
packets = generate(num_packets)


for packet in packets: # Output a summary of each packet
    print(packet.summary())
        






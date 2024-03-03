# Packet Analysis Simulation Software

This repository contains a packet analyser simulation software developed in Python using the Scapy library. The software generates both clean and malicious packets in IPv4 for simulation and analysis purposes.

## Overview

Packet analysis is essential in network forensics for identifying performance issues and managing traffic effectively. This allows analysts to monitor, detect, and respond to suspicious network anomalies, enhancing network security.

## Features

- ### Packet Generation:
  The software generates a random number of clean and malicious packets with random IP addresses and ports
- ### Clean Packets:
  Simulates normal network traffic with random source and destination IP addresses
- ### Malicious Packets:
  Simulates harmful network activity such as port scanning and suspicious ICMP messages
- ### Packet Summary:
  Displays a description of the packets detailing if they are clean or malicious

## Getting Started

### Prerequisites:
- Python 3.x installed on your system
- Install Scapy library using pip
  
  ```
  pip install scapy
  ```

### Usage

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/habahmadi/packetAnalyser.git
   ```

2. Navigate to the project directory:

   ```
   cd packetAnalyser
   ```
   
3. Run the python script

## Future Additions

- GUI Implementation: Implement a simple GUI to visualise packet generation and analysis
- Analysis Tools: Add functionality to analyse packet contents and detect patterns

## Contributing

Contributions are welcome! If you have ideas for new features, find bugs, or want to improve the software, feel free to submit a pull request.

   
   

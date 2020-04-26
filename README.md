# Active_fuzzer
Corresponding code to the paper "Active Fuzzing for Testing and Securing Cyber-Physical Systems" by authors: Yuqi Chen, Bohan Xuan, Christopher M. Poskitt, Jun Sun and Fan Zhangin in ISSTA2020.
This project is created to test **SWaT**, a testbed located in SUTD.

# Requirement
## Hardware
1.Four raspberry Pis or order devices with a Linux OS.  
2.One laptop with a Linux OS  
3.USB Ethernet adaptors  
4.Ethernet cable extenders  

## Software
python 2.7.16  
matplotlib 2.2.4  
netfilter 0.6.4  
numpy 1.16.2  
pandas 0.24.1  
pyzmq 18.0.1  
scapy 2.4.2  
scikit-learn 0.20.3  
tcpdump 4.9.2  
# Setup

1. Physical connect the Raspberry Pis to all PLCs in level0.  
2. Edit and run start_lvl0 to enable bridge-netfilter to set up bridges for all Raspberry Pis.

# Usage


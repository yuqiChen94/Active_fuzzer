# Active_fuzzer
Corresponding code to the paper "Active Fuzzing for Testing and Securing Cyber-Physical Systems" by authors: Yuqi Chen, Bohan Xuan, Christopher M. Poskitt, Jun Sun, and Fan Zhang in ISSTA2020. This project is created to test **SWaT**, a testbed located in SUTD.


# Requirement
## Hardware
1.Four raspberry Pis with a wireless network adapter and an ethernet adapter  
2.One laptop with a Linux OS  
3.USB Ethernet adaptors  
4.Ethernet cable extenders  

## Software
python 2.7.16    
matplotlib 2.2.4 (https://matplotlib.org/)   
netfilter 0.6.4 (https://www.netfilter.org/)  
numpy 1.16.2  (https://numpy.org/)  
pandas 0.24.1 (https://pandas.pydata.org/)  
pyzmq 18.0.1  (https://pyzmq.readthedocs.io/en/latest/)  
scapy 2.4.2 (https://scapy.net/)    
scikit-learn 0.20.3 (https://scikit-learn.org/)  
tcpdump 4.9.2  (https://www.tcpdump.org/manpages/tcpdump.1.html)  
# Setup

1. Physically connect the Raspberry Pis to all PLCs in level0. (USB Ethernet adaptors are used here since Raspberry Pis typically has only one ethernet port.) 
2. Edit and run start_lvl0.sh to enable bridge-Netfilter to set up bridges for all Raspberry Pis.
3. Make sure all the Raspberry Pis and the laptop are put onto the same wireless subnet.     


# Code structure
This project contains three modules:
* Packet collection
* Active learning
* Attack implications


# Usage
### Data collection
For each Raspberry Pi, edit and run script tcpdump.sh to sniff packets in level 0 for different PLC.  
Collect corresponding sensor value from the dataset in the meantime.  
Run the script extract_bits.py and extra_log.py to generate the feature vectors and sensor values used for training.  
### Active learning
For each Raspberry Pi, edit and run the corresponding stage_server.py and stage_client.py. In the meantime, run main_client.py and main_server.py on the laptop. These scripts are used to pass all the packets from different PLCs to one laptop.   
Edit and run active_learning.py to active manipulate and packets and update the model. 
### Attack implications
..

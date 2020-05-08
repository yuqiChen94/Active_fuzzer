For each stage,'stage*_server.py' is the zmq server which send message from raspberry pi to laptop,while doing active learning,the message contains: 

1.'capture flag.txt' 
To help main controller in laptop determine whether the pi has formed a vector from the level0 packets.The active learning progress will continue only when all 4 capture_flags are True.

2.'stage*old.txt'
Vector extracted from the level0 packets in each stage,it will be sent to laptop to construct a new vector.

3.'pv_diff.txt'
The label for each vector

'stage*_client.py' is the zmq client which receive message from laptop,while doing active learning,the message contains: 

1.'new_vector.txt'
After active learning,a new vector will be sent to pi,it will reconstruct to packets and sent to plc.

2.stage_states
To synchronously control all four stages

'stage*_AL.py' is the code to deal with level0 packets using netfilterqueue and scapy.

AL_utils.py contains some functions and utilities to simplify code writing.

CIP_sequence.py is the scapy code to dissect connection ID and sequence number in enip protocol.


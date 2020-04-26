modprobe br_netfilter
echo 1 >/proc/sys/net/ipv4/ip_forward
echo 1 >/proc/sys/net/bridge/bridge-nf-call-iptables
sudo ifconfig br0 down
sudo brctl delbr br0
sudo brctl addbr br0
sudo brctl addif br0 enp3s0 enx000ec6b75a5b
sudo ifconfig enp3s0 up
sudo ifconfig enx000ec6b75a5b up 
sudo ifconfig br0 up

#change enx000ec6a76988, enx9cebe8aea755  interface accordingly to yours. 


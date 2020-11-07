#!/bin/bash 
ip=$(hostname -I) 
pub=$(curl ifconfig.me)
echo $ip >>nmap.txt
echo $pub >>nmap.txt
nmap $ip >> nmap.txt
nmap --script http-headers scanme.nmap.org >>nmap.txt
nmap $pub >>nmap.txt
base64 nmap.txt >> nmapcoded.txt

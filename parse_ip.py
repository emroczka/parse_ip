#!/usr/bin/env python3
import sys
import ipaddress


if len(sys.argv) != 2:
    print ("Usage: parse_ip.py <IP_Address_textfile>")
    print (" e.g    : parse_ip.py <targetlist>")
    print ("Output will be dumped to the screen. Use redirection to send it to a file.")
    sys.exit(1)

def ip_range(x):
    # split the range into its two IP Address components
    ips = x.split(" - ")
    # get the 1st IP Address in the range. Strip it of whitespace characters
    start=ipaddress.IPv4Address(ips[0].strip(" "))
    # get the 2nd IP Address in the range. Strip it of whitespace characters
    end=ipaddress.IPv4Address(ips[1].strip(" "))
    # Loop through the IP Addresses
    for i in range(int(start),int(end)):
        print(ipaddress.IPv4Address(i))
    print(end)

# open the file passed as an argument
with open(sys.argv[1],"r") as file:
    line=file.read()

    for ip in line.split(","):
        if ip.find(" - ") > 0:
            # call function ip_range to enumerate the ip range to stdout
            ip_range(ip)
        else:
            # write the single ip address to stdout
            print(ip)

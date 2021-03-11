# parse_ip
parse IP Addresses into format usable by other tools (i.e. nmap)

I needed a way to convert the output provided to me from a large, well known,
vulnerability scanner and convert it into a list of the IP addresses for use
by other tools. In this case I am specifically going to use the output as a
target list for nmap.

The original output from the vulnerability scanner provides a list of single
IP Addresses and IP Address ranges delimited by commas. No cidr notation is 
included with either the single addresses (/32) or the ip address ranges (/24,
/22, or whatever).

This is my first useful python script. And my first published repository in
github.

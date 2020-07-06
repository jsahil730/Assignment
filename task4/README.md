# Task 4

Imo this was an easy task if you know how to google for stuff.
I initially was thinking that the provided zip would be encrypted as well, but that's not the case lol.

So umm since I didn't know much about the 802.11 protocol, I thought maybe the pcap file contains the hash :thinking:

I tried to read some of the packets, didn't understand any of the stuff, and no clues to any hash so far.

Next, I think maybe the JTR has some tool to extract something from pcap files, there is a python2 script in the folder named `pcap2john.py` but it didn't do shit.
  
So next I tried googling stuff, hit upon [this](https://null-byte.wonderhowto.com/how-to/hack-wi-fi-cracking-wpa2-psk-passwords-using-aircrack-ng-0148366/) link. Oh it says you can use `aircrack-ng` to crack the password if you know the wordlist where it could exist, and that too only with the pcap file, dayummmmmm this tool is awesome!  
Almost there! Install aircrack-ng, and simply say `aircrack-ng friday.pcap -w wordlist.txt` and it gives you the password `bhavesh007bhavika`.

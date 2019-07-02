#!/usr/bin/python3

import os

rr = '\033[0m'     #reset
bold = '\033[01m'
d = '\033[02m'     #disable
ul = '\033[04m' #underline
reverse = '\033[07m'
st = '\033[09m' #strikethrough
invis = '\033[08m'#invisible
white = '\033[0m'
cwhite = '\33[37m'
black ='\033[30m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lgrey = '\033[37m'
grey = '\033[90m'
lred = '\033[91m'
lgreen = '\033[92m'
yellow = '\033[93m'
lblue = '\033[94m'
pink = '\033[95m'
lcyan = '\033[96m'
bgreen = '\33[42m'
blgreen = '\33[102m'
bred = '\33[41m'
blred = '\33[101m'
borange = '\33[43m'
byellow = '\33[33m'
bcyan = '\33[44m'
blcyan = '\33[104m'
br = '\33[108m'
brown = '\33[33m'
bwhite = '\33[107'

def clear():
    x = 0
    while x <= 4:
        os.system("clear")
        x = x + 1

def help(cracker):
    if cracker == "WEP":
        print("The " + cracker + " Cracker has the following commands:")
        print("""        > exit
        > ls <LOCATION>
        > scan
        > probe <BSSID> <CH>
        > crack <LOCATION>""")
        print("""
    exit - Use this command to leave the WEP cracker and go back to the main mode.

    ls <LOCATION> - Use this command to list your directories in order to find your wep files are.
        - LOCATION: This is the directory you are looking into for files

    scan - Use this command to scan the area for active WEP/WPA/WPA2 networks within a range. It will display
        - ESSID: The friendly network name you see in the Network Manager.
        - BSSID: The network device address, used for probing and cracking.
        - CH: Short for channel in which the wireless device is operating on. Used for probing.
        - PWR: The strength that the signals carry, lower the better.

    probe <BSSID> <CH> - Used to attack a wireless network to flood the network and extract the WEP Key
        - BSSID: The network device ID to which you will want to target.
        - CH: Short for channel in which the wireless device is operating on. Used for probing.

    crack <LOCATION> Used to crack the password of a wireless network.
        - LOCATION: The directory to where the ./wep file is.
    """)
    else:
        print("The " + cracker + " Cracker has the following commands:")
        print("""        > exit
        > ls <LOCATION>
        > scan
        > capture <BSSID> <CH>
        > crack <BSSID> <PASSWORDLIST> <LOCATION>""")
        print("""
    exit - Use this command to leave the WEP cracker and go back to the main mode.

    ls <LOCATION> - Use this command to list your directories in order to find your .cap files.
       - LOCATION: This is the directory you are looking into for files

    scan - Use this command to scan the area for active WEP/WPA/WPA2 networks within a range. It will display
        - ESSID: The friendly network name you see in the Network Manager.
        - BSSID: The network device address, used for probing and cracking.
        - CH: Short for channel in which the wireless device is operating on. Used for probing.
        - PWR: The strength that the signals carry, lower the better.

    capture <BSSID> <CH> - Used to capture one of the handshakes in order to crack the network password.
        - BSSID: The network device ID to which you will want to target.
        - CH: Short for channel in which the wireless device is operating on. Used for capturing the handshake.

    crack <BSSID> <PASSWORDLIST> <LOCATION> Used to crack the password of a wireless network.
        - BSSID: The network device ID to which you will want to target.
        - PASSWORDLIST: The directory to where your password list is.
        - LOCATION: The directory to where the .cap file is.
    """)

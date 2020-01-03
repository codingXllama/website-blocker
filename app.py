# Web blocker python program
"""

The Host file on mac is located in: /etc/hosts
The Host file on Windows is located in: C:\Windows\System32\drivers\etc

"""

import time
from datetime import datetime as dt

# creating a raw string via \\ or using 'r' letter infront of the string
windows_Hostpath = r"C:\Windows\System32\drivers\etc"
redirection_IP_route = "127.0.0.1"

websites_toBlock = ["www.gmail.com", "gmail.com"]
currentTime = dt(dt.now().year, dt.now().month, dt.now().day, 8)
timeToBlock = dt(dt.now().year, dt.now().month, dt.now().day, 10)


if currentTime == timeToBlock:
    print("time to block")
else:
    print("no block")


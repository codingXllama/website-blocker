# Web blocker python program
"""

The Host file on mac is located in: /etc/hosts
The Host file on Windows is located in: C:\Windows\System32\drivers\etc

"""

import time
from datetime import datetime as dt


# Creating a temp host file, that we can alter and then use it to override the systems original host file
temp_HostFile = "hosts"

# creating a raw string via \\ or using 'r' letter infront of the string
windows_Hostpath = r"C:\Windows\System32\drivers\etc"

# The the required the redirection file that will be used to block desired sites
redirection_IP_route = "127.0.0.1"


websites_toBlock = ["https://mail.google.com/", "www.gmail.com"]
# currentTime = dt(
#     dt.now().year, dt.now().month, dt.now().day, dt.now().hour, dt.now().minute
# timeToBlock = dt(dt.now().year, dt.now().month, dt.now().day, dt.now().hour, 18)

startingMinutes=int(input("Enter the starting minutes: "))
endingMinutes=int(input("Enter the Ending minutes: "))
while True:

    # checking the status of the time in regards the hours (present vs blocking time hours)
    if dt(dt.now().year, dt.now().month, dt.now().day, dt.now().hour, startingMinutes ) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, dt.now().hour, endingMinutes):
        print("time to block")
        with open(temp_HostFile,'r+') as tempHostFile:
            hostFileContent=tempHostFile.read()
            for website in websites_toBlock:
                if website in hostFileContent:
                    pass
                else:
                    tempHostFile.write(f"{redirection_IP_route} {website}\n")
                    
    else:                   
        print("no block")
    # The program will now sleep for n-seconds, before rechecking the time
    time.sleep(2)


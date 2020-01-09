# Web blocker python program
"""

The Host file on mac is located in: /etc/hosts
The Host file on Windows is located in: C:\Windows\System32\drivers\etc

"""


# /usr/bin/python
import time
from datetime import datetime as dt


# Creating a temp host file, that we can alter and then use it to override the systems original host file
windows_Hostpath = "hosts"

# creating a raw string via \\ or using 'r' letter infront of the string
windows_Hostpath = r"C:\Windows\System32\drivers\etc\hosts"

# The the required the redirection file that will be used to block desired sites
redirection_IP_route = "127.0.0.1"
redirection_IP_route2 = "140.82.113.4"


websites_toBlock = [
    "https://www.mail.google.com/",
    "https://www.youtube.com/",
    "https://mail.google.com/mail/u/0/#inbox",
    "https://mail.google.com/",
    "www.https://mail.google.com/",
    "www.gmail.com",
    "https://mail.google.com/mail/u/0/#inbox",
    "https://www.google.com/intl/en-GB/gmail/about/",
    "https://www.github.com/",
]


startingMinutes = int(input("Enter the starting minutes: "))
endingMinutes = int(input("Enter the Ending minutes: "))
while True:

    # checking the status of the time in regards the hours (present vs blocking time hours)
    if (
        dt(dt.now().year, dt.now().month, dt.now().day,
           dt.now().hour, startingMinutes)
        < dt.now()
            < dt(dt.now().year, dt.now().month, dt.now().day, dt.now().hour, endingMinutes)):
        print("time to block")
        with open(windows_Hostpath, "r+") as myFile:
            hostFileContent = myFile.read()
            for website in websites_toBlock:
                if website in hostFileContent:
                    pass
                elif website == "www.youtube.com":
                    print("I'm on github, I have been redirected to :D")
                    myFile.write(f"{redirection_IP_route2} {website}\n")
                else:
                    myFile.write(f"{redirection_IP_route} {website}\n")

    else:
        """
        The purpose of this else block is to open the host files
        and then write the required files to be blocked, if they already exist,
          then we don't write them again
        """
        with open(windows_Hostpath, "r+") as myFile:

            # opening the already existing host file and then storing each line in  a variable called ' hostFileContent'
            hostFileContent = myFile.readlines()

            # placing the file pointer just before the start of the file content
            myFile.seek(0)
            for line in hostFileContent:
                # if the website in the lines we read is not stored in the websites to block list, then we will write that line to the host file
                if not any(website in line for website in websites_toBlock):
                    myFile.write(line)

            # cutting out all the written text after the end of file
            # basically it's purpose here is to revert the changes that has happened to the file (writting to the file)
            myFile.truncate()
        # The program will now sleep for n-seconds, before rechecking the time
        print("Fun hours....")
    time.sleep(10)

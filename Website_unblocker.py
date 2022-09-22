import platform
import sys

websites=[]

def remover(websites):
    if platform.system() == "Windows":
        pathToHosts=r"C:\Windows\System32\drivers\etc\hosts"
    elif platform.system() == "Linux":
        pathToHosts=r"/etc/hosts"

    with open(pathToHosts,'r+') as file:
      content=file.readlines()
      file.seek(0)
      for line in content:
        if not any(site in line for site in websites):
            file.write(line)
      file.truncate()

 

while True:
    print("Enter the website's URL which you want to unblock.\n Once you finish writing the URL, type 'done'.")
    while True:
        str = input() 
        if str == "done":
            break
        else:
            websites.append(str)

    remover(websites)
    print("Unblocked. If you want to quit, press 'q'.")
    str = input()

    if str == "q":
        sys.exit()
    else:
        pass
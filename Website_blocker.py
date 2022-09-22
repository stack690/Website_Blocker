import platform
import sys

websites = []
def add(websites):
  if platform.system() == "Windows":
        pathToHosts=r"C:\Windows\System32\drivers\etc\hosts"
  elif platform.system() == "Linux":
        pathToHosts=r"/etc/hosts"

  redirect="127.0.0.1"

  with open(pathToHosts,'r+') as file:
    content=file.read()
    for site in websites:
        if site in content:
            pass
        else:
            file.write(redirect+" "+site+"\n")

while True:
    print("Enter the website's URL which you want to block.\n Once you finish writing the URL, type 'done'.")
    while True:
        str = input() 
        if str == "done":
            break
        else:
            websites.append(str)

    add(websites)
    print("Blocked. If you want to quit, press 'q'.")
    str = input()

    if str == "q":
        sys.exit()
    else:
        pass
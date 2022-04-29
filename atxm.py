import requests
from time import ctime, sleep, time
import cryptography
import time
from bs4 import BeautifulSoup
import os
import subprocess
from colorama import Fore


print(Fore.GREEN + """

  ______   ________  __    __  __       __ 
 /      \ /        |/  |  /  |/  \     /  |
/$$$$$$  |$$$$$$$$/ $$ |  $$ |$$  \   /$$ |
$$ |__$$ |   $$ |   $$  \/$$/ $$$  \ /$$$ |
$$    $$ |   $$ |    $$  $$<  $$$$  /$$$$ |
$$$$$$$$ |   $$ |     $$$$  \ $$ $$ $$/$$ |
$$ |  $$ |   $$ |    $$ /$$  |$$ |$$$/ $$ |
$$ |  $$ |   $$ |   $$ |  $$ |$$ | $/  $$ |
$$/   $$/    $$/    $$/   $$/ $$/      $$/ .py
( https://github.com/n000b-n000b ^_^ )
-------------------------------------------""")
print(ctime())
print("-----------------------------------------")
def main():
  Webserver = ["Apache HTTP Server", "IIS", "Nginx", "lighttpd", "Jigsaw Web Server", "Klone Web Server", "Abyss Web Server", "Oracle Web Tier", "Xitami Web Server", "Zeus Web Server", "LiteSpeed Web Server", "Jetty", "AOLserver", "WEBrick", "Cherokee", "Virtusoso Unicersal Server", "Hiawatha", "Oracle iPlanet Web Server", "Resin", "Yaws", "NaviServer", "thttpd", "Monkey HTTP Server", "Jexus", "NCSA HTTPd", "HTTP File Server", "Caudium", "Boa", "Mongoose", "Tengin", "Gunicorn", "Adobe JRun", "Mongrel", "Tornado" ]
  file = open('rootdomains.txt', 'r+')
  count = 0
  dic = {}
  urls = file.readlines()
  for i in urls:
    count += 1
    dic[count] = i.strip()
    f = open(i.strip(), 'w')
    try:
      r = requests.get('https://' + i.strip(), timeout=5)
      print("-------------------------------------------------")
      print(count, "  | ", i.strip(), " | Status:", + r.status_code)
      
      sleep(0.7)
      if (r.status_code == 200):
        f.write(r.text)
      else:
        continue
    except:
      print("-------------------------------------------------")
      print(i.strip() + " Failed to respond. Manual inspection advised")
main()

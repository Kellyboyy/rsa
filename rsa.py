#Aahil_coding
import os, time, platform
os.system("cd $HOME/")

try:
    import futures
except ImportError:
    os.system("pip2 install futures")

try:
    import lolcat
except ImportError:
    os.system("pip2 install lolcat")
try:
    import requests
except ImportError:
    os.system("pip2 install requests")
    os.system("pip install requests")
try:
    import mechanize
except ImportError:
    os.system("pip2 install mechanize")
    os.system("pip install mechanize")
rana=platform.architecture()[0]
if rana=="32bit":
    import rsa32bit
    rsa32bit.main_system()
elif rana=="64bit":
    import rsa64bit
    rsa64bit.main_system()

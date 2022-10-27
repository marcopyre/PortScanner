import netifaces
import os
from netaddr import IPAddress

def getInterfaces():
    return netifaces.interfaces()


def formatAddress(interface):
    addrs = netifaces.ifaddresses(interface)
    pcaddress = addrs[netifaces.AF_INET][0]['addr'].split('.')
    return pcaddress[0] + '.' + pcaddress[1] + '.' + pcaddress[2] + '.0/' + str(
        IPAddress(str(addrs[netifaces.AF_INET][0]['netmask'])).netmask_bits())


os.system("rustscan -a " + formatAddress(getInterfaces()[-1]) + " --ulimit 5000")

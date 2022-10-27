import netifaces
import os
from netaddr import IPAddress

def getInterfaces():
    return netifaces.interfaces()


def formatAddress(interface):
    addrs = netifaces.ifaddresses(interface)
    try:
        pcaddress = addrs[netifaces.AF_INET][0]['addr'].split('.')
        return pcaddress[0] + '.' + pcaddress[1] + '.' + pcaddress[2] + '.0/' + str(
            IPAddress(str(addrs[netifaces.AF_INET][0]['netmask'])).netmask_bits())
    except:
        return ''

print('-------------------------\nchoose the interface to use:')

running = True


while running == True:
    interfaces = getInterfaces()
    nullinterfaces = []
    counter = 1
    for interface in interfaces:
        address = formatAddress(interface)
        if address != '':
            print('[' +  str(counter) + '] ' + address  + '(' + interface + ')')
            counter+=1
        else:
            nullinterfaces.append(interface)

    for nullinterface in nullinterfaces:
        interfaces.remove(nullinterface)

    try:
        choice = input()
        address = formatAddress(interfaces[int(choice) - 1])
        os.system("rustscan -a " + address + " --ulimit 5000")
        running = False
    except:
        print('invalid input')



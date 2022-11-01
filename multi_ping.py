from operator import index
import threading, time, random, os, subprocess
import subprocess
from datetime import datetime
from inputimeout import inputimeout, TimeoutOccurred
from colorama import init, Fore, Style
from pprint import pprint

refreshtime = 1
server_list = {}
# Color selectors
red = Style.RESET_ALL + Fore.RED
green = Style.RESET_ALL + Style.BRIGHT + Fore.GREEN
yellow = Style.RESET_ALL + Fore.YELLOW
# Set CMD window size
os.system('mode 44,30')

# Get current working directory
cwd = os.getcwd()
os.system('cls')
server_list_file = 'server_list.txt'
# Generate dictonary from external server list file
if os.path.isfile(server_list_file):
    with open(server_list_file) as f:
        for line in f:
            (name, ip) = line.split(',')
            server_list[name] = ip.strip()
else:
    print(red + '\n Error: server_list.txt file not found.\n Make sure the server_list.txt is on root as ping tool\n')
    time.sleep(5)
    exit()

results = []
print(len(server_list))


def logger(host, name, delay):
    # time.sleep(delay)
    # print("In Func: " + str(delay))

    ip = str(host)

    # Building the command. Ex: "ping -c 1 google.com"
    command = 'ping -n 1 ' + ip + " | findstr \"TTL\""
    # print(command)
    p = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL)
    p.wait()
    # print (p.poll())

    if p.poll() == 0:
        results.append(str(name + " " + ip + " Online"))
    else:
        results.append(str(name + " " + ip + " Offline"))
    # print(ip)


test = ''
print("Number of active threads: " + str(threading.activeCount()))


def runner():
    for server_name, server_ip in server_list.items():
        delay = int(random.random())
        thread = threading.Thread(target=logger, args=(server_ip, server_name, delay))
        thread.start()


def checker():
    while (threading.activeCount() > refreshtime):
        if (len(results) == len(server_list)):
            os.system('cls')
            # print ("Number of active threads: " + str(threading.activeCount()))
            results.sort()
            # print("Results len is: " + str(len(results)))
            for i in results:
                if ("Offline" in i):
                    print('{:>8s}'.format(red + i))
                else:
                    print('{:>8s}'.format(green + i))
            # pprint(results)
            time.sleep(20)


while (True):
    runner()
    checker()
    results = []
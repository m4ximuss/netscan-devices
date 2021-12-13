import os
import platform
import threading
import socket
from datetime import datetime

def get_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.connect(('<broadcast>', 0))
    return s.getsockname()[0]

def scan_ip(ip):
    addr = net + str(ip)
    comm = ping_com + addr
    response = os.popen(comm)
    data = response.readlines()
    for line in data:
        if 'TTL' in line:
            print(addr, "--> Ping Ok")
            break

net = get_my_ip()
print('You IP :',net)
net_split = net.split('.')
a = '.'
net = net_split[0] + a + net_split[1] + a + net_split[2] + a
start_point = int(input("Enter the Starting Number: "))
end_point = int(input("Enter the Last Number: "))

oc = platform.system()
if (oc == "Windows"):
    ping_com = "ping -n 1 "
else:
    ping_com = "ping -c 1 "

t1 = datetime.now()
print("Scanning in Progress:")

for ip in range(start_point, end_point):
    if ip == int(net_split[3]):
       continue
    potoc = threading.Thread(target=scan_ip, args=[ip])
    potoc.start()

potoc.join()
t2 = datetime.now()
total = t2 - t1

print("Scanning completed in: ", total)
import sqlite3

con = sqlite3.connect('new.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS addresses(ip INTEGER)')
cur.executive('INSERT INTO addresses(ip) VALUES addr')

con.commit()

cur.close()
con.close()

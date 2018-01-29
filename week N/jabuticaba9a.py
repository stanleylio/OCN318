# Advanced Topic: UDP Communications
# "It's not meant to squeeze lemons, it is meant to start conversations."
#
# Run broadcast.py and transmit.py in two separate terminals.
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18

from socket import *


IP = '255.255.255.255'
PORT = 50008
sock = socket(AF_INET,SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET,SO_BROADCAST,1)


who = gethostname()
while True:
    what = input('Say something: ')
    m = '{} said: {}'.format(who, what)
    #print('broadcasting: ' + m)
    sock.sendto(m.encode(),(IP,PORT))

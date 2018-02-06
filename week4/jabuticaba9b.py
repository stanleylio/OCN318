# Advanced Topic: UDP Communications
# "It's not meant to squeeze lemons, it is meant to start conversations."
#
# Run broadcast.py and transmit.py in two separate terminals.
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18

import socket


IP = ''
PORT = 50008
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((IP,PORT))

print('Listening...')
while True:
    data,addr = sock.recvfrom(1024)
    print(data.decode())

'''
Briefing L04 C05
Alien Server
So, it seems the aliens are using what looks like human technology and we've identified they're running a server. We need you to try and connect to the server and see what's going on.

Instructions:

Connect to the server ("localhost", 10000).
Send USER followed by aliensignal.
Then send PASS followed by unlockserver.
Then SEND followed by moonbase.
Then send END and you should get access.
Tip: Get access to the server using the above instructions to get the flag.
'''

#----------------------------------------------------------------------------------

#
# Connect to alien server ('localhost', 10000),
# Then send USER followed by aliensignal,
# Then send PASS followed by unlockserver,
# Next SEND followed by moonbase.
# Then send END and if all followed key will provided.
#
# Note: You must receive data back from the server after you send each message
#

#----------------------------------------------------------------------------------

# SOLUTION

# Then send USER followed by aliensignal,
# Then send PASS followed by unlockserver,
# Next SEND followed by moonbase.
# Then send END and if all followed key will provided.
#
# Note: You must receive data back from the server after you send each message
#

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 10000))

clientsocket.send(b'USER')
print(clientsocket.recv(1024))
clientsocket.send(b'aliensignal')
print(clientsocket.recv(1024))

clientsocket.send(b'PASS')
print(clientsocket.recv(1024))
clientsocket.send(b'unlockserver')
print(clientsocket.recv(1024))

clientsocket.send(b'SEND')
print(clientsocket.recv(1024))
clientsocket.send(b'moonbase')
print(clientsocket.recv(1024))

clientsocket.send(b'END')
print(clientsocket.recv(1024))


data = clientsocket.recv(4096)
print(data)

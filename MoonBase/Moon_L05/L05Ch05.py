# Briefing L05 C05
# Jovian Tweets
# This is a bit weird, but looking at the files the aliens are sending would suggest they are trying to find a way to post messages on social media back on Earth. Maybe it's part of a co-ordinate attack to spread panic. We better figure out how they are doing it, and the best way is probably to try it yourself using the protocols they seem to be using.

# Some instructions:

# Write a script that uses a web API to create a social media post.
# There is a tweet bot API listening at http://127.0.0.1:8082, GET / returns basic info about the API.
# POST / with x-api-key:tweetbotkeyv1 and data with user tweetbotuser and a status-update of alientest.
# Tip: Read the response to get the flag.

#-----------------------------------------------------

#
# Tweet bot API listening at http://127.0.0.1:8082.
# GET / returns basic info about api. POST / with x-api-key:tweetbotkeyv1
# and data with user tweetbotuser and status-update of alientest
#

#--------------------------------------------------------

# SOLUTION
#
# Tweet bot API listening at http://127.0.0.1:8082.
# GET / returns basic info about api. POST / with x-api-key:tweetbotkeyv1
# and data with user tweetbotuser and status-update of alientest
#
import urllib.parse
import urllib.request

url = "http://127.0.0.1:8082/"
header={"x-api-key" : 'tweetbotkeyv1'}
post_param = urllib.parse.urlencode({
                    'user' : 'tweetbotuser',
           'status-update' : 'alientest'
          }).encode('UTF-8')

req = urllib.request.Request(url, post_param, header)
response = urllib.request.urlopen(req)

print(response.read())

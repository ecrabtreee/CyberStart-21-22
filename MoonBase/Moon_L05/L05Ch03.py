# Briefing L05 C03
# Alien Zip
# Wow, things are getting crazy, the aliens have flooded us with cryptic zip files and we've no idea what's inside them or, for that matter, how and why they seem to be using human technology in their communications with us.

# Anyway, we've started organising the files to try and make sense of them, but they're all locked with a numerical three-digit passcode. See if you can write a script to get into this example file alien-zip-2092.zip and read the text file inside which we think is named whatever the zip is (so in this case alien-zip-2092.txt). Oh, by the way, files should be extracted to the /tmp/ directory.

# Tip: Extract the file to the /tmp/ directory to get the flag. Make sure to break out of the loop when you hit the correct password, otherwise you will override the correct file with a blank one with the same name.

#-----------------------------------------------------------------

#
# Sample Alien Zip file found at /tmp/alien-zip-2092.zip is password protected
# We have worked out they are using three digit code
# Brute force the Zip file to extract to /tmp
#
# Note: The script can timeout if this occurs try narrowing
# down your search

#---------------------------------------------------------------

# SOLUTION

#
# Sample Alien Zip file found at /tmp/alien-zip-2092.zip is password protected
# We have worked out they are using three digit code
# Brute force the Zip file to extract to /tmp
#
# Note: The script can timeout if this occurs try narrowing
# down your search
import zipfile
import itertools

digits = '0123456789'

for c in itertools.product(digits, repeat=3):
  password = ''.join(c)
  try:
    with zipfile.ZipFile('/tmp/alien-zip-2092.zip', 'r') as zip_ref:
      zip_ref.extractall(path='/tmp', pwd = bytes(password, 'utf-8'))
      break
  except:
    print('Password ' + password + ' failed')
    
pwd = bytes(password, 'utf-8')

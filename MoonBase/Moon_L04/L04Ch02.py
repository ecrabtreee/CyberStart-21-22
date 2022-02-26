# Briefing L04 C02
# Agent Profiles
# The operations team have asked that we start preparing a group of agents that could be sent on a mission to intercept the alien craft. We need to review the profiles of our agents, but the script we wrote to get them (they live in different places, e.g. /tmp/agent-1 and /tmp/agent-2) seems to be broken. Can you fix it?

# Tip: Fix and run the script to get the flag.

#------------------------------------------------


# Fix the below script to read from each agent file found in /tmp.
# Example agent profile would be /tmp/agent-1.txt
# The contents of each of the agent files makes up the flag
#


import os.path

count = 1

for i in range(20):
fname = "/tmp/agent-" + str(count)+".txt"
if os.path.isfile(fname):
with open(fname, 'r') as content_file:
content = content_file.read()
print(content.rstrip())
count += 1

#-------------------------------------------------------

# SOLUTION

#
# Fix the below script to read from each agent file found in /tmp.
# Example agent profile would be /tmp/agent-1.txt
# The contents of each of the agent files makes up the flag
#


import os.path

count = 1

for i in range(20):
  fname = "/tmp/agent-" + str(count)+".txt"
  with open(fname, 'r') as content_file:
      content = content_file.read()
      print(content.rstrip())
  if os.path.isfile(fname):
    count += 1
    
# Flag = The output given

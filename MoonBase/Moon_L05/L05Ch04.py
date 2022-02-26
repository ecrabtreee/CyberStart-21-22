'''
Briefing L05 C04

Passphrase Panic
So, things are moving quickly and one of our agents has just pointed out to me that we should probably get on the defensive and make sure all our files are locked and have secure passphrases. We need your help to generate those passphrases.

We've already created a script that generates 3 random numbers that correspond to the position of words that can be found in the /tmp/words.txt file. You will find those numbers in the wordNumbers array.

Instructions:

Use these randomly generated numbers in wordNumbers to create a passphrase using the words from /tmp/words.txt.
For example, if wordNumbers = ['1', '60', '2'] then you need to get the 2nd word from words.txt. Then the 61st word. Then the 3rd word.
Put a space between each word and print the result as the generated passphrase.
Tip: Generate a passphrase to get the flag.
'''

#-----------------------------------------------------------------

#
# Write a script to generate a passphrase by taking words from
# /tmp/words.txt
# The wordNumbers array holds three random numbers. Each number
# corresponds to a word in words.txt. So for example
# wordNumbers[1] is the second word in /tmp/words.txt.
# Put a space between each word and print it out
#


with open("/tmp/randomwordsnumbers.txt", "r") as file:
    data = file.read()

wordNumbers = data.rstrip().split("\\n")

#----------------------------------------------------------------

# SOLUTION


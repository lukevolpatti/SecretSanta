################
# Secret Santa #
################

# Dependencies: yagmail, keyring, random
# Instructions:
# 1. Follow steps on yagmail github repository to set up email environment
# 2. Create text file with names of participants and their email addresses,
#    one participant per line. Format: Nick Frost nick.frost@northpole.com
#    Name file "people.txt"
# 3. Make sure people.txt is in the same folder as this script and make sure
#    that your email address is entered below.
# 4. Run the script: python3 santa.py
# 5. Everyone will be emailed their matches!


import yagmail
from random import shuffle

# Sender's email address
yag = yagmail.SMTP('me@example.com')

# Text file that will be read from
# File must be in appropriate format
myfile = open("people.txt", "r")
data = myfile.readlines()

# Create dictionary of participants
dict = {}
for line in data:
	words = line.split()
	dict[words[0] + " " + words[1]] = [words[2]]

# Create list of names and randomize
names = list(dict.keys())
shuffle(names)

# Step through randomized list of names
# Assign each name to the subsequent name
size = len(names)
for i in range(size):
	contents = ['You will be buying a gift for: ' + names[(i+1) % size]]
	yag.send(dict[names[i]], 'Secret Santa!', contents)

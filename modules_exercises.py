#print an alphabetically sorted list of all functions in the re module, which contain the word find

import re

# Your code goes here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))
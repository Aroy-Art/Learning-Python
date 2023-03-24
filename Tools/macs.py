#!/bin/python3


# input string, i.e. "xx:xx:xx:xx:xx:xx,xx:xx:xx:xx:xx:xx"
macs_raw = "00:04:A5:A3:3B:B0,00:27:22:56:60:8D,00:27:22:56:68:DA,00:27:22:56:69:EC,00:27:22:56:6F:6B,00:27:22:56:6F:6B"

# split the input string of mac address with a ","
macs = macs_raw.split(",")

def list_duplicates(seq):
  seen = set()
  seen_add = seen.add
  # adds all elements it doesn't know yet to seen and all other to seen_twice
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
  # turn the set into a list (as requested)
  return list( seen_twice )

# get the duplicates for the list_duplicates() function
dups = list_duplicates(macs)

# Print number of duplicates
print("Found %s duplicate(s)." % (len(dups)))

# print a list of all duplicates
for i in dups:
    print(i)


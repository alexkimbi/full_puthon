# Option 1 
#Note, dictionaries are read byt "keys" and not by values onlike "list"
ages = { 'kelvin': 42, 'Alex': 32, 'bob': 40 }
ages.keys()                 # This will provide the dictionary keys (such as kelvin, Alex and Bob without their values)
print(ages)                 # This prints the mames and ages  for all stored in the dictionary
print(ages['Alex'])         # This prints the  age of Alex 

#option 2
ages.items()                # This prints  you with the name of the items store in the dictionary 
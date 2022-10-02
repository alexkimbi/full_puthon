#!/usr/bin/env python3.7

#python implimentation goes here
fahrenheit = float(input("What temp (in fahrenheit) would you like to convert to celsuis? "))
celsuis = (fahrenheit - 32) * 5 / 9 # formular to get the Celsuis
print(fahrenheit, "F is equal to ",  round(celsuis, 2 ), "C") # The round 2 makes it to round the anser to two decimal place
print(fahrenheit, "F is",  round(celsuis, 2 ), "C") # The round and 2 rounds the output to two decimal places


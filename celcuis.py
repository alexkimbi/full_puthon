#!/usr/bin/env python3.7

#python implimentation goes here
fahrenheit = float(input("What temp (in fahrenheit) would you like to convert to celsuis? "))
celsuis = (fahrenheit - 32) * 5 / 9

print(fahrenheit, "F is",  round(celsuis, 2 ), "C")

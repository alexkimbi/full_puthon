#!/usr/bin/env pyhon3.7
msg = input("Enter a message: ")
print("first Character:", msg[0])
print("last character:", msg[-1])
print("middle character :", msg[int(len(msg) /2)])
print("Even index charaters:", msg[0::2])
print("odd index Character:", msg[1::2])
print("Reversed message:", msg[::-1])

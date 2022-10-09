#/usr/bin/env python3.7
upper_number = int(input("How many values should we process: ")) # should be a number devisible by 3 and 5 (e.g 15,  30)
for number in range(1, upper_number +1 ):
    if number % 3 == 0 and number % 5 == 0: # number divisible by 3 and 5 
        print(f"works, the number you selected is {number}")
    elif number % 3 == 0:
        print("The number is divisible by 3")
    elif number % 5 == 0:
        print(f" {number} is devisible by 5")
    else:
        print(number)
                
name = input("what is your name? ")
color = input("What is your favorite color? ")
age = int(input("how old are you? "))
#print(name "is " + str(age) + "and is a" + color "guy" and  + ".")
#print(name, end=" ")
#print("is " + str(age) + " years old", end=" ")
#print("and loves the  color "+ color + ".", end=" ")
print(name, 'is', age, 'years old and loves the color', color +'.', sep=" ")

import random
ec2_num = int(input("How manay number of EC2 instances do you want? "))
dept = ('Finance','Marketing','Technology','HR')
chrs = 'abcdef0123456789' # Change your required characters here
n = 10 # Change your word length here

print(''.join(random.choices(chrs, k=10)))
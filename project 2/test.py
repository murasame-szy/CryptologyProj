import random

List = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*_'
List = list(List)
mesg1 = ''
i = 0
while i < 16:
    mesg1 = mesg1 + random.choice(List)
    i += 1
print(mesg1)
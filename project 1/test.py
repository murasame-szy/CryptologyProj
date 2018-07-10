from DES import *

msg = input('message: ')
key = input('key: ')
n = input('round: ')
c = des(msg, key, 16)
print('\n\n\n')
print('Encryption:')
print('cipher is ' + c)

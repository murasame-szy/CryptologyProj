#-*- coding: utf-8 -*-

from DES import *
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import random

def create_key():
    List = '0123456789abcdef'
    List = list(List)
    i = 0
    key1 = ''
    while i < 16:
        key1 = key1 + random.choice(List)
        i += 1
    return key1

def change_key(key1):
    mesg_encode = encode(key1)
    change_num = 8
    while change_num % 8 == 0:
        change_num = random.randint(1, 64)
    if mesg_encode[change_num - 1] == '1':
        mesg_encode = mesg_encode[:(change_num - 1)] + '0' + mesg_encode[change_num :]
    else:
        mesg_encode = mesg_encode[:(change_num - 1)] + '1' + mesg_encode[change_num :]
    c = 0
    for a in mesg_encode:
        if a == '0':
            c += 1
        else:
            break
    key2 = hex(int(mesg_encode, 2))[2:]
    if c >= 4:
        key2 = '0' * int(c / 4) + key2
    return key2

def countchange(mesg1, key1, key2, n):
    m1 = des(mesg1, key1, n)
    m2 = des(mesg1, key2, n)
    m1_hex = encode(m1)
    m2_hex = encode(m2)
    c = compare(m1_hex, m2_hex)
    return c

def main():
    X = []
    Y = []

    n = 1
    while n <= 16:
        i = 1
        c = 0
        while i <= 1000:
            mesg1 = create_key()
            print('mesg1: ' + mesg1)
            key1 = create_key()
            print('key1' + key1)
            key2 = change_key(key1)
            print('key2' + key2)
            c = c + countchange(mesg1, key1, key2, n)
            i += 1
        c = c / 1000
        print('average count: ' + str(c) + '\n\n\n')
        Y.append(c)
        X.append(n)
        n = n + 1

    # 绘制图
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
    fig = plt.figure()
    plt.plot(X, Y, linewidth=1,color='r',marker='o', markerfacecolor='blue',markersize=5)
    plt.xlabel(u"加密轮数", fontproperties=font)
    plt.ylabel(u"密文变化比特数", fontproperties=font)
    plt.title(u"改变一比特密钥密文变化图", fontproperties=font)
    plt.grid(X)
    plt.show()

main()
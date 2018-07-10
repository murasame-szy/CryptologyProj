import math
import collections
import numpy as np
import matplotlib.pyplot as plt

#非常用性
def dic(key):
    file = open("a.txt")
    for i in file.readlines():
        i = i[:-1]
        if i == key:
            return 0
    return 150

#复杂度
def exhaustive(key):
    l = len(key)
    grade_len = l * 4
    List1 = '0123456789'
    List2 = 'abcdefghijklmnopqrstuvwxyz'
    List3 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    List4 = '!@#$%&*_'
    List1 = list(List1)
    List2 = list(List2)
    List3 = list(List3)
    List4 = list(List4)
    c1 = [0, 0, 0, 0]
    for i in key:
        if i in List1:
            c1[0] += 1
        elif i in List2:
            c1[1] += 1
        elif i in List3:
            c1[2] += 1
        elif i in List4:
            c1[3] += 1
    #长度*4，数字个数*2，（l-小写字母）*2，大写相同，字符*6
    grade_len = grade_len + c1[0] * 2 + (l - c1[1]) * 2 + (l - c1[2]) * 2 + c1[3] * 6
    #四类，少一类除以2
    for i in c1:
        if i == 0:
            grade_len = grade_len / 2
    if grade_len > 150:
        grade_len = 150
    return grade_len

def Random(key):
    #统计各字符个数，返回字典
    b = {a: key.count(a) for a in set(key.replace(' ', ''))}
    h = 0
    for i in key:
        p = b[i] / len(key)
        h = h - math.log(p, 2)
    #熵乘10
    h = h / len(key) * 15
    #扣分基础100
    grade_random = 150 + h
    #重复，扣n(n-1)*5
    for i in b.items():
        grade_random = grade_random - i[1] * (i[1] - 1) * 10
    i = 0
    a = 0
    List = []
    while i < (len(key) - 1):
        List.append(ord(key[i + 1]) - ord(key[i]))
        i += 1
    for i in List:
        if i == 1:
            a += 1
        elif i == -1:
            a += 1
    grade_random =grade_random - a * 40
    return grade_random

# #非关联性
# def relation(key):
#


def main():
    key = input('please input the key\n')
    grade_dic = dic(key)
    grade_len = exhaustive(key)
    grade_random = Random(key)
    labels = np.array(['非常用性', '复杂度', '随机性'])
    dataLenth = 3
    List = []
    List.append(grade_dic)
    List.append(grade_len)
    List.append(grade_random)
    data = np.array(List)

    angles = np.linspace(0, 2 * np.pi, dataLenth, endpoint=False)
    data = np.concatenate((data, [data[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, data, 'ro-', linewidth=2)
    ax.set_thetagrids(angles * 180 / np.pi, labels, fontproperties="SimHei")
    ax.set_title("密码强度", va='bottom', fontproperties="SimHei")
    ax.grid(True)
    plt.show()



main()
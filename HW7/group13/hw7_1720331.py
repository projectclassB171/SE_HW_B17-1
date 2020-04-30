# coding=gbk
#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。

import math
def 最大公约数最小公倍数():
    a,b=map(int,input('题目一,请输入两个正整数作为参数：').split())
    d = math.gcd(a,b)
    x = (a*b)//d
    tupl = (d,x)
    print("题目一的输出结果为;",tupl)#第一个元素为最大公约数，第二个元素为最小公倍数.
最大公约数最小公倍数()




#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。

def 字符串计数():
    num_number = char_number = space_number = other_number = 0
    str_2 = input("题目二,请输入一个字符串:")
    for char in str_2:
        if char.isdigit():
            num_number += 1
        elif char.isalpha():
            char_number += 1
        elif char == ' ':
            space_number += 1
        else:
            other_number += 1
    print("题目二输出结果,数字个数：%d,字母个数：%d,空格个数：%d,其他字符：%d" % (num_number,char_number,space_number,other_number))
字符串计数()

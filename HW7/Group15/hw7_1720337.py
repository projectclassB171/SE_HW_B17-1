''''''
import re
'''
1.编写函数，接收两个正整数作为参数，返回一个元组，
其中第一个元素为最大公约数，第二个元素为最小公倍数。
'''
import math
def demo(x, y):
    if x> y:
        x, y = y, x
    all = x* y
    while x!= 0:
        j = y % x
        y = x
        x= j
    return (y, int(all / y))
print(demo(15, 30))

'''
2.编写函数，接受一个字符串作为参数，
计算并打印传入字符串中数字，字母，空格，以及其它的个数。
'''
def demo(str):
    num =zimu =space=other = 0
    for i in s:
        if i.isdigit():
            num += 1
        elif i.isalpha():
            zimu += 1
        elif i.isspace():
            space += 1
        else:
            other += 1
s = input("输入字符串:")
print(demo(s))

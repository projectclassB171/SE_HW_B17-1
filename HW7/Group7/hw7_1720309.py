"""1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。"""
import re
def a(x, y):
    b = 1
    i = 2
    max1 = max(x, y)
    while i <= max1:
        if y % i == 0 and x % i == 0:
            b *= i
            y /= i
            x /= i
            i = 2
        else:
            i += 1
    bei = int(b * x * y)
    return (b, bei)
n1, n2 = input("请输入两个正整数").split()
z = a(int(n1), int(n2))
print(z)

"""2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。"""

def count(s):
    number = 0
    letter = 0
    space = 0
    others = 0
    for i in s:
        if i.isdigit():
            number += 1
        elif i.isalpha():
            letter += 1
        elif i.isspace():
            space += 1
        else:
            others += 1
    print('数字的个数：{}\t字母的个数：{}\t空格的个数：{}\t其他的个数：{}'.format(number, letter, space, others))
count(input("请输入一个字符串："))








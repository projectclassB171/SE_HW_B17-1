#1.编写函数，接收两个正整数作为参数，返回一个元组，
# 其中第一个元素为最大公约数，第二个元素为最小公倍数。
import math
def gcdAndlcm(m,n):
    a = math.gcd(m,n)
    b = (m*n)//a
    return (a,b)
m,n = input("请输入两个正整数:").split()
result = gcdAndlcm(int(m),int(n))
print("最大公约数和最小公倍数分别是：",result)
print()
print()
#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def count_n(m):
    n_num = 0
    n_letter = 0
    n_space = 0
    n_other = 0
    for i in m:
        if i.isdigit():
            n_num+=1
        elif i.isalpha():
            n_letter+=1
        elif i.isspace():
            n_space+=1
        else:
            n_other +=1
    print("字符串中数字，字母，空格，以及其它的个数分别是：",n_num,n_letter,n_space,n_other)
msg = input("请输入一串字符，包括数字，字母，空格和其他：")
count_n(msg)

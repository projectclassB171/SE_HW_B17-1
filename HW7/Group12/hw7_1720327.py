# 题目 1

import math
def demo():
    a, b = map(int, input("请输入两个正整数：").split())
    c = math.gcd(a, b)
    d = (a*b)//c
    print("最小公约数为：",c)
    print("最大公倍数为：",d)
demo()

# 题目 2

def demo():
    a = 0   # 数字
    b = 0   # 字母
    c = 0   # 空格
    d = 0   # 其他
    str = input("请输入你想要的字符串：")
    for i in str:
        if i.isdigit():
            a += 1
        elif i.isalpha():
            b += 1
        elif i.isspace():
            c += 1
        else:
            d += 1
    print("在你输入的字符串中，数字个数为:%d，字母个数为：%d，空格个数为：%d，其他个数为%d" % (a,b,c,d))
demo()

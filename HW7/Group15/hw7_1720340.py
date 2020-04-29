# 题目一
# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
# 定义函数

import math
def getTuple(n1, n2):
    t1 = math.gcd(n1, n2)
    tm1 = int(n1 * n2 / t1)
    tmu1 = (t1, tm1)
    return tmu1

print(getTuple(3, 10))


# 题目二
# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。

def calculateStr(str):
    num = 0
    le = 0
    sp = 0
    oth = 0
    for s in str:
        if s.isdigit():
            num += 1
        elif s.isspace():
            sp += 1
        elif (65 <= ord(s) <= 90) or (97 <= ord(s) <= 122):
            le += 1
        else:
            oth += 1
    return num, le, sp, oth
t2 = "hudhusdn李昀燕1720340。。。"
result = calculateStr(t2)
print("需要计算的字符串为："+t2 + "\n"+"其中中：数字有{}个；字母有{}个；空格有{}个；其他字符有：{}个".format(result[0], result[1], result[2], result[3]))


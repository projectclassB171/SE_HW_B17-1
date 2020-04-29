import math


# 题目一
# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
# 定义函数
def getTuple(num1, num2):
    divisor = math.gcd(num1, num2)  # 最大公约数，math.gcd()求最大公约数
    multiple = int(num1 * num2 / divisor)  # 公倍数
    tul = (divisor, multiple)  # 结果元组
    return tul


print(getTuple(23, 45))


# 题目二
# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def calculateStr(str):
    number = 0  # 数字个数
    letter = 0  # 字母个数
    space = 0  # 空格个数
    others = 0  # 其他的个数
    for s in str:
        if s.isdigit():  # isdigit 判断有没有数字
            number += 1
        elif s.isspace():  # isspace 判断有没有空格
            space += 1
        elif (65 <= ord(s) <= 90) or (97 <= ord(s) <= 122):  # isalpha 判断有没有字符
            letter += 1
        else:
            others += 1
    return number, letter, space, others


str1 = "Aabc我我我我1234zZ //"
result = calculateStr(str1)
print(str1 + "字符串中：数字有{}个；字母有{}个；空格有{}个；其他字符有：{}个".format(result[0], result[1], result[2], result[3]))

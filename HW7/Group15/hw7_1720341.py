import re

'''
2.编写函数，接收两个正整数作为参数，返回一个元组，
其中第一个元素为最大公约数，第二个元素为最小公倍数。
'''


# 定义一个函数hcflcm(x,y)
def hcflcm(x, y):
    # 该函数返回两个数的最大公约数与最小公倍数

    # 获取最小值（返回最大公约数）
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(2, smaller + 1):
        if (x % i == 1) and (y % i == 0):
            hcf = i

    #  获取最大的数(返回最小公倍数)
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return hcf, lcm


num1 = int(input("1-1.请输入第一个正整数："))
num2 = int(input("1-2.请输入第二个正整数："))
res = hcflcm(num1, num2)

print("结果：",num1, "和", num2, "的最大公约数为：", res[0], "；最小公倍数为：", res[1])
print()



'''
2.编写函数，接受一个字符串作为参数，
计算并打印传入字符串中数字，字母，空格，以及其它的个数。
'''


def count(str):
    counts = {'数字': 0, '字母': 0, '空格': 0, '其他': 0}

    # re.search匹配整个字符串，直到找到一个匹配
    for i in str:
        if re.search('\d', i):
            counts['数字'] += 1
        elif re.search('[a-z,A-Z]', i):
            counts['字母'] += 1
        elif re.search('\s', i):
            counts['空格'] += 1
        else:
            counts['其他'] += 1
    return counts


str = input("2.请随意输入一个字符串：")

print(count(str))

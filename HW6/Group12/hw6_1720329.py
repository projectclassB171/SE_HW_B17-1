# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。


def fun(m, n):
    if m > n:
        m, n = n, m
    p = m * n
    while m != 0:
        r = n % m
        n = m
        m = r
    return n, int(p // n)


print(fun(5, 30))


# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数


def count_string(s):
    num = space = alpha = other = 0
    for i in s:
        if i.isdigit():
            num += 1
        elif i.isalpha():
            alpha += 1
        elif i.isspace():
            space += 1
        else:
            other += 1
    print("数字的个数是{}".format(num))
    print("字母的个数是{}".format(alpha))
    print("空格的个数是{}".format(space))
    print("其他字符的个数是{}".format(other))


a = input("请输入一个字符串：")
count_string(a)

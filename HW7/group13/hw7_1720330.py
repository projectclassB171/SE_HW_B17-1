'''
1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
'''
def demo(a, b):
    c = 0
    z = a * b
    while c == 0:
        try:
            if a % b == 0:
                c = b
            else:
                a = b
                b = a % b
        except ZeroDivisionError:
            c = 1
    d = int(z / c)
    return c, d
print(demo(15, 8))

'''
2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
'''
def d2(str):
    number = 0
    letter = 0
    blank = 0
    other = 0
    for i in range(0,len(str)):
        if 48 <= ord(str[i]) <= 57:
            number += 1
        elif (65 < ord(str[i]) <= 90) or (97 <= ord(str[i]) <= 122):
            letter += 1
        elif ord(str[i]) == 32:
            blank += 1
        else:
            other += 1
    print("该字符串中数字有%d个,字母%d个,空格%d个,其他的%d个." % (number, letter, blank, other))


string = input("请输入一个字符串:")
d2(string)

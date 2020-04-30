#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def demo(a,b):
    p = a*b
    while a%b != 0:
        a,b = b,a%b
    return(b,p//b)
print(demo(20,30))

#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def count(str):
    num,alp,space,other = 0,0,0,0
    for i in str:
        if i.isdigit():
            num += 1
        elif i.isalpha():
            alp += 1
        elif i.isspace():
            space += 1
        else:
            other += 1
    print('数字的个数：{}\n字母的个数：{}\n空格的个数：{}\n其他的个数：{}'.format(num, alp, space, other))
str = input("请输入字符串：")
count(str)
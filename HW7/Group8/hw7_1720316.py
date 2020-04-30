#<1>编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def demo(a,b):
    if a>b:
        a,b=b,a
    p=a*b
    while a!=0:
        s=b%a
        b=a
        a=s
    return (b,int(p/b))
print(demo(2,21))

#<2>编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def count(s):
    numb=0
    alpha=0
    space=0
    other=0
    for i in s:
        if i.isdigit():
            numb +=1
        elif i.isalpha():
            alpha +=1
        elif i.isspace():
            space +=1
        else:
            other +=1
    print('数字:{},字母:{},空格:{},其他:{}'.format(numb,alpha,space,other))
count(input("请输入一个字符串："))


#题目1
#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def main(x,y):
    #比较x，y,互换机制，较大值赋值给y，较小值赋值给x
    if x > y:
        x, y = y, x
    a = x*y
    while x!=0:
        #%取余数
        b = y%x
        y = x
        x = b
    return (int(a/y),y)
print(main(54,24))

#题目2
#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def jishu(s):
    al_num = 0     #字母
    space_num = 0  #空格
    digit_num = 0  #数字
    other = 0      #其他
    for i in s:
        if i.isdigit():    # isdigit 判断有没有数字
            digit_num+= 1
        elif i.isspace():   # isspace 判断有没有空格
            space_num+= 1
        elif i.isalpha():    #isalpha 判断有没有字母
            al_num+= 1
        else:
            other+= 1
    print('英文字符数{},数字字符数{},空格字符数{},其他字符数{}'.format(al_num, digit_num, space_num, other))
jishu('aks;ldjfl;kasjdflk23481723u98471   #@#@')
jishu(input("请输入一个字符串："))


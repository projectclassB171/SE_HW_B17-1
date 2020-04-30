'''
1.编写函数，接收两个正整数作为参数，返回一个元组，
  其中第一个元素为最大公约数，第二个元素为最小公倍数。
'''
import math
def common():
    a,b=map(int,input('题目一,请输入两个正整数作为参数：').split())
    d = math.gcd(a,b)
    x = (a*b)//d
    tupl = (d,x)
    print("题目一的输出结果为;",tupl)#第一个元素为最大公约数，第二个元素为最小公倍数.
common()



'''
2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中
  数字，字母，空格，以及其它的个数。
'''
def countString():
    num_sum = string_sum = space_sum = other_sum = 0
    str_2 = input("题目二,请输入一个字符串:")
    for char in str_2:
        if char.isdigit():
            num_sum += 1
        elif char.isalpha():
            string_sum += 1
        elif char == ' ':
            space_sum += 1
        else:
            other_sum += 1
    print("题目二输出结果,数字个数：%d,字母个数：%d,空格个数：%d,其他字符：%d" % (num_sum,string_sum,space_sum,other_sum))
countString()
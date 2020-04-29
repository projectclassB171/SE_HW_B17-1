''''''
import re
'''
1.编写函数，接收两个正整数作为参数，返回一个元组，
其中第一个元素为最大公约数，第二个元素为最小公倍数。
'''
def common(x,y):
    yue = 1
    i = 2
    max1 = max(x,y)
    while i<=max1 :
        if y%i==0 and x%i==0:
            yue *= i
            y /= i
            x /= i
            i = 2
        else:
            i += 1

    bei = int(yue*x*y)

    return (yue,bei)

n1,n2 = input("请输入两个正整数").split()
a = common(int(n1),int(n2))
print(a)

'''
2.编写函数，接受一个字符串作为参数，
计算并打印传入字符串中数字，字母，空格，以及其它的个数。
'''
def count(str):
    dict = {'数字':0,'字母':0,'空格':0,'其他':0}
    for i in str:
        if re.search('\d',i):
            dict['数字'] += 1
        elif re.search('[a-z,A-Z]',i):
            dict['字母'] += 1
        elif re.search('\s', i):
            dict['空格'] += 1
        else:
            dict['其他'] += 1
    return dict


s = input("请输入一个字符串")

print(count(s))

''''''
import re
'''
1.��д����������������������Ϊ����������һ��Ԫ�飬
���е�һ��Ԫ��Ϊ���Լ�����ڶ���Ԫ��Ϊ��С��������
'''
import math
def demo(x, y):
    if x> y:
        x, y = y, x
    all = x* y
    while x!= 0:
        j = y % x
        y = x
        x= j
    return (y, int(all / y))
print(demo(15, 30))

'''
2.��д����������һ���ַ�����Ϊ������
���㲢��ӡ�����ַ��������֣���ĸ���ո��Լ������ĸ�����
'''
def demo(str):
    num =zimu =space=other = 0
    for i in s:
        if i.isdigit():
            num += 1
        elif i.isalpha():
            zimu += 1
        elif i.isspace():
            space += 1
        else:
            other += 1
s = input("�����ַ���:")
print(demo(s))

#(1)�������ַ�����PHP�滻ΪPython


t='best_language = PHP is the best programming language in the world! '
t1=t.replace('PHP','python')
print(t1)

#(2)��д���룬��ʾ�û�����1-7�߸����֣��ֱ������һ�����գ���ӡ������������ܼ���


s="һ������������"
c=eval(input("������1-7�ڵ����֣�"))
if c in range(1,8):
 print("����Ϊ����{}".format(s[c-1]))

#(3)����һ���ַ����� Python is the BEST programming Language����дһ��������ʽ�����жϸ��ַ����Ƿ�ȫ��ΪСд


import re

best_language = "PHP is the best programming language in the world! "
rule = '[a-z]+$'
result = re.search(rule, best_language)
if result:
    print('ȫ��ΪСд')
else:
    print('����ȫ��ΪСд')

#��4����ȡһ���ַ�����Ҫ��ʹ��������ʽ����ȡ���еĵ绰���룬�绰����ĸ�ʽ�ٶ�Ϊ����xxx�� xxx-xxxx��xxx-xxx-xxxx��


def find(a):
 phone = re.findall(r"(\d{3})\-(\d{3})\-(\d{4})|\((\d{3})\)\s(\d{3})\-(\d{4})", a)
 print("phone: ", phone)
str2 = input("������һ�����е绰������ַ���:")
find(str2)

#��5������������ʽ�����в�ͬ���ַ����л�ȡָ����ʽ�����ڡ����ڵĸ�ʽΪyyyy-mm-dd��
#     '������2022/9/24', '������2017/09/25', '������2012-07-25', '������2020��04��25',


DateText = ['������2022/9/24', '������2017/09/25', '������2012-07-25', '������2020��04��25']
result = []
rule1 = r'(\d{4}).(\d{1,2}).(\d{1,2})'
for string in DateText:
    result.append(re.findall(rule1, string))
for oneResult in result:
    for item in oneResult:
        print(item[0], item[1], item[2], sep='-')
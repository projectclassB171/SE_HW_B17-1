# coding=gbk
#1 �������ַ�����PHP�滻ΪPython      
#best_language = "PHP is the best programming language in the world! "
best_language = "PHP is the best programming language in the world!"
keyWord = "PHP"
print(best_language.replace(keyWord, "Python"))

#2 ��д���룬��ʾ�û�����1-7�߸����֣��ֱ������һ�����գ���ӡ������������ܼ���
weeks = "һ������������"
num = eval(input("������1-7�ڵ����֣�"))
if num in range(1, 8):
    print("��{}".format(weeks[num - 1]))

#3 ����һ���ַ����� Python is the BEST programming Language��
#��дһ��������ʽ�����жϸ��ַ����Ƿ�ȫ��ΪСд��
import re

line = "Python is the BEST programming Language!"
res = r'^[a-z\s]*$'
if re.match(res, line):
    print("ȫ��Сд!")
else:
    print("��ȫ��Сд!")

#4  ��ȡһ���ַ�����Ҫ��ʹ��������ʽ����ȡ���еĵ绰���룬�绰����ĸ�ʽ�ٶ�Ϊ��
#��xxx�� xxx-xxxx��xxx-xxx-xxxx��
import re
lines = input("�������������ַ�����")
phone = re.findall(r'\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}', lines)
print("".join(phone))

#5 ����������ʽ�����в�ͬ���ַ����л�ȡָ����ʽ�����ڡ����ڵĸ�ʽΪyyyy-mm-dd��
#'������2022/9/24', '������2017/09/25', '������2012-07-25', '������2020��04��25',
import re
text = '������2022/9/24, ������2017/09/25, ������2012-07-25, ������2020��04��25'
result = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", text)
print("".join(res))

# 1.�������ַ�����PHP�滻ΪPython

best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))

# 2.��д���룬��ʾ�û�����1 - 7
# �߸����֣��ֱ������һ�����գ���ӡ������������ܼ���

num_input = input("������1-7�߸����֣�")
print("��������{}".format(num_input))

# 3.����һ���ַ����� Python is the BEST programming Language��
# ��дһ��������ʽ�����жϸ��ַ����Ƿ�ȫ��ΪСд��

import re
best_language = "PHP is the best programming language in the world! "
x = '[a-z]+$'  
result = re.search(x, best_language) 
if result:
    print('ȫ������Сд')
else:
    print('����ȫ��Сд')

# 4.��ȡһ���ַ�����Ҫ��ʹ��������ʽ����ȡ���еĵ绰���룬�绰����ĸ�ʽ�ٶ�Ϊ��
# ��xxx�� xxx - xxxx��xxx - xxx - xxxx��

#��D���ļ�data.txt�б��������µļ���
#789-123-4567
#123 456 7890
#(456) 123-7890

import re
def setPhoneNumber():
    phoneLines = open(r"D:\eclipse_python\eclipse_workplace\src\data.txt","r")
    for phoneLine in phoneLines:
        phoneLine = phoneLine.strip('\n')
        if re.findall("(\d{3})\-(\d{3})\-(\d{4})", phoneLine):
            print phoneLine
        if re.findall("\((\d{3})\)\s(\d{3})\-(\d{4})", phoneLine):
            print phoneLine
if __name__=="__main__":
    setPhoneNumber()


# 5.����������ʽ�����в�ͬ���ַ����л�ȡָ����ʽ�����ڡ����ڵĸ�ʽΪyyyy - mm - dd��
# '������2022/9/24,������2017/09/25,������2012-07-25,������2020��04��25'

import re
pattern = re.compile(r"(\d{4}-\d{1,2}-\d{1,2})"#����ƥ��ģʽ

string = '������2022/9/24, ������2017/09/25, ������2012-07-25, ������2020��04��25'
print re.findall(pattern,string)
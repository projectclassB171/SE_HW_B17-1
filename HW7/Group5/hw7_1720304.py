# 1.��д����������������������Ϊ����������һ��Ԫ�飬���е�һ��Ԫ��Ϊ���Լ�����ڶ���Ԫ��Ϊ��С��������

def demo(m,n):
    p = m*n
    while m%n != 0:
        m,n = n,m%n
    return(n,p//n)

print(demo(12, 45))

#���н����(3, 180)

# 2.��д����������һ���ַ�����Ϊ���������㲢��ӡ�����ַ��������֣���ĸ���ո��Լ������ĸ�����

s=input('input a string:\n')
char=0
space=0
digit=0
others=0
for c in s:
    if c.isalpha():     #isalpha �ж���û���ַ�
        char+=1
    elif c.isspace():   # isspace �ж���û�пո�
        space+=1
    elif c.isdigit():   # isdigit �ж���û������
        digit+=1
    else:
        others+=1
print('char=%d,space=%d,digit=%d,others=%d'%(char,space,digit,others))

#��������input a string:
#"ylionman0802 "
#char=8,space=1,digit=4,others=2
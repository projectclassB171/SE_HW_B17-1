#1.��д����������������������Ϊ����������һ��Ԫ�飬���е�һ��Ԫ��Ϊ���Լ�����ڶ���Ԫ��Ϊ��С��������
def demo(x,y):
  z = x*y
  while x%y != 0:
      x,y = y,x%y
  return(y,z//y)

print(demo(33, 44))

#���н��:
(11, 132)


#2.��д����������һ���ַ�����Ϊ���������㲢��ӡ�����ַ��������֣���ĸ���ո��Լ������ĸ�����
def count(s):
  numbe,alpha,space,other = 0,0,0,0
  for i in s:
      if i.isdigit():
          numbe += 1
      elif i.isalpha():
          alpha += 1
      elif i.isspace():
          space += 1
      else:
          other += 1

  print('���֣�{}\t��ĸ��{}\t�ո�{}\t������{}'.format(numbe,alpha,space,other))
count(input("������һ���ַ�����"))

#���н��:
������һ���ַ�������feawf˾����2370����/��   ��fe
���֣�4	��ĸ��12	�ո�3	������4
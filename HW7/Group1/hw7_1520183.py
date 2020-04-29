#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def demo(x,y):
  z = x*y
  while x%y != 0:
      x,y = y,x%y
  return(y,z//y)

print(demo(33, 44))

#运行结果:
(11, 132)


#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
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

  print('数字：{}\t字母：{}\t空格：{}\t其他：{}'.format(numbe,alpha,space,other))
count(input("请输入一个字符串："))

#运行结果:
请输入一个字符串：法feawf司法俄2370，。/。   的fe
数字：4	字母：12	空格：3	其他：4
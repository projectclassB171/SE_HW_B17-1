# 题目<1>:编写函数，接收两个正整数作为参数，返回一个元组，
# 其中第一个元素为最大公约数，第二个元素为最小公倍数。
def demo(m, n):
    if m > n:
        m, n = n, m
    mul = m * n
    while m != 0:
        x = n % m
        n = m
        m = x
    return (n, int(mul / n))


print(demo(20, 30))

# 题目<2>:编写函数，接收一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其他的个数。
def string(s):
  num, alpha, space, other = 0, 0, 0, 0
  for i in s:
    if i.isdigit():
        num += 1
    elif i.isalpha():
        alpha += 1
    elif i.isspace():
        space += 1
    else:
        other += 1
  print('英文字符数{},数字字符数{},空格字符数{},其他字符数{}'.format(alpha,num,space,other))
string(input("请输入一个字符串："))

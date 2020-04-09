# coding=utf-8
x = 0
while x <= 30:
    y = 30 - x
    if 2 * x + 4 * y == 90:
        print '鸡有', x, "个,兔有", y, '个'
        break
    x = x + 1

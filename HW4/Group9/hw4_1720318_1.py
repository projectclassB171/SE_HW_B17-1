# coding=utf-8
x = 0
while x <= 20:
    y = 0
    while y <= 33:
        z = 100 - x - y
        if 5 * x + y * 3 + z / 3.0 == 100:
            print '公鸡', x, '只,母鸡', y, '只,小鸡', z, '只'
        y = y + 1
    x = x + 1

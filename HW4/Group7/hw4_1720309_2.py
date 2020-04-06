a = 0
b = 0
while a <= 30 and b <= 30:
    if a + b == 30:
        print('鸡%d只",兔%d' % (a, b))
    if 2*a + 4*b == 90:
        print('鸡%d只,兔%d只' % (a, b))
        break
    a += 1
    b = 30 - a

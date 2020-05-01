# coding=utf-8
print '第一题'


def f1(a, b):
    x = a
    y = b
    while b != 0:
        temp = a % b
        a = b
        b = temp
    r1 = a
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            r2 = greater
            break
        greater += 1
    result = (r1, r2)
    return result


print f1(54, 24)
print '第二题'


def f2(str):
    num = 0
    let = 0
    sp = 0
    oth = 0
    for s in str:
        if s.isdigit():
            num += 1
        elif s.isspace():
            sp += 1
        elif (65 <= ord(s) <= 90) or (97 <= ord(s) <= 122):
            let += 1
        else:
            oth += 1
    return num, let, sp, oth


print f2('dasdcx55zc zxASD哈哈s   54999916$%+++^#%')

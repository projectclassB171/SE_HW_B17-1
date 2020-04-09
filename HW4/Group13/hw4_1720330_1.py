for a in range(100 // 5 + 1):
    for b in range(100 // 3 + 1):
        for c in range(0, 100 * 3 + 1, 3):
            if a + b + c == 100 and a * 5 + b * 3 + (c // 3) * 1 == 100:
                print('公鸡:%d 母鸡:%d 小鸡:%d' % (a, b, c))

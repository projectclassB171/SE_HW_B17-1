count = 0
for big in range(1, 100):
    for middle in range(1, 100):
        for small in range(1, 100):
            if big * 3 + middle * 2 + small / 3 == 100:
                if big + middle + small == 100:
                    count += 1
                    print("第" + str(count) + "种", end=": ")
                    print("公鸡的只数为", big, end=" ")
                    print("母鸡的只数为", middle, end=" ")
                    print("小鸡的只数为", small)
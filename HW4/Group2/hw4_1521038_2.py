for rabbit in range(1, 30):
    for chicken in range(1, 30):
        if rabbit+chicken == 30:
            if rabbit*4+chicken*2 == 90:
                print("兔子有：", rabbit, "鸡有：", chicken)
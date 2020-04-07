a = 30 #a为鸡兔总数
b = 90 #b为脚总数
for x in range(1, a):
    y = a - x
    if 2 * x + 4 * y == b:
        print("已知鸡兔总数共30只，脚共90只可：得鸡有" + str(x) + "只，兔有" + str(y) + "只。")

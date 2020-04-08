'''
2.鸡兔同笼问题。
假设共有鸡、兔30只，脚90只，
求鸡、兔各有多少只?
'''

foots = 90
num_all = 30

for c_num in range(0,30):   
    r_num = 30 - c_num
    if c_num*2+r_num*4 == foots:
        print("鸡有{}只,兔有{}只".format(c_num,r_num))
        break

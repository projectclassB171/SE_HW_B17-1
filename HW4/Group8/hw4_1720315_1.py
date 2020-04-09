money=100                                   #现有100元

score=0                                     #花出去的钱现为0元

for x in range(21):                         #设买公鸡的个数为x，且最多能买20只公鸡

    for y in range(34):                     #设买母鸡的个数为y，且最多能买33只母鸡

        for z in range(301):                #设买小鸡的个数为z,且最多能买300只小鸡

            score=5 * x + 3 * y + z / 3     #花出的钱列方程为5x+3y+z/3

            if score==money and x+y+z==100: #'=='为判断，左右是否相等的意思

                print('公鸡是%s只，母鸡是%s只，小鸡是%s只'%(x,y,z))
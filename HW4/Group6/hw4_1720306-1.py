money=100

score=0

for x in range(21):

    for y in range(34):

        for z in range(301):

            score = 5 * x + 3 * y + z / 3

            if score == money and x+y+z == 100:

                print('公鸡是%s只，母鸡是%s只，小鸡是%s只'%(x,y,z))
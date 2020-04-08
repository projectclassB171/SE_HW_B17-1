for x in range(0,21):
    for y in range(0,34):
        for z in range(0,301):
            if (x*5 +y*3 +z/3==100)&(x+y+z==100):
                print("公鸡:",x,"母鸡",y,"小鸡",z,"\n")

for x in range(0,100//5):
    for y in range(0,100//3):
        for z in range(0,100):
            if x*5 +y*3 +z/3==100 and x+y+z==100:
                 print("公鸡:",x,"母鸡",y,"小鸡",z,"\n")
	
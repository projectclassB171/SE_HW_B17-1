'''
一：2k = -9  变量名不能是数字开头
二：if缩进量错误
三：with属于关键字，不能作为变量使用
四：数字不能直接与字符串拼接；
五：混用引号、双引号错误
'''
k = -9
if k>= 0:
    jieguo= str(k) + "正数"
    print(jieguo)
else:
    print(str(k) + "负数")
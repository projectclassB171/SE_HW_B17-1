'''
错误一：2k = -9  变量名不能是数字开头；
错误二：缩进量不符合规定；
错误三：with属于关键字，不能作为变量使用；
错误四：数字不能直接与字符串拼接；
错误五：混用引号、双引号；
'''
k = -9
if k>= 0:
    res= str(k) + "正数"
    print(res)
else:
    print(str(k) + "负数")
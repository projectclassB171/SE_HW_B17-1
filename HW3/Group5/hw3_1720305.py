#第三次作业
#错误
#1、2k变量名不能是数字开头 
#2、缩进要保持一致
#3、with是关键字，不能用作变量名使用
#4、混合使用引号、双引号
#5、数字不能与字符串直接拼接


#改正如下
k = -9
if k>=0:
    r=str(k)+"正数"
    print(r)
else:
    print(str(k)+"负数")
#第三次作业：
#2k = -9
#错误：数字不能作为变量名开头
#  if 2k>= 0:
#错误：数字不能作为变量名开头
#    with = 2k +"正数"
#错误：数字不能作为变量名开头；with是关键字，不能用于变量名
#        print(with)
#错误：修改with变量名；不需要再缩进，与上一句同缩进即可。
#    else:
#错误：不需要缩进
#    print(2K+ '负数")
#错误：变量名错误；单双引号引用不成功，需要配对；数据类型不一致不可用+连接




#改正代码：
#***********First**************
_2k = -9
 if _2k>=0:
	withs = str(_2k) + "正数"
	print(withs)
else:
	print(_2k,'负数')
	
#-9 负数

#***********Second**************
'''
_2k = -9
 if _2k>=0:
	withs = str(_2k) + '正数'
	print(withs)
else:
	print(_2k,"负数")
'''
	
#-9 负数
#************Third****************
"""
_2k = -9
 if _2k>=0:
	withs = str(_2k) + '正数'
	print(withs)
else:
	print(str(_2k)+"负数")

	
-9负数
"""
#************Fourth*********************
'''
_2k = -9
 if _2k>=0:
	withs = str(_2k) + '正数'
	print(withs)
else:
	print(str(_2k)+"\n负数")

	
-9
负数
'''
#*************Fifth*********************
"""
_2k = 9
 if _2k>=0:
	withs = str(_2k) + '\t正数'
	print(withs)
else:
	print(str(_2k)+"负数")

	
9	正数
"""

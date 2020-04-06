#错误原因：
#2k = -9    变量名不能以数字开头，可加上英文、数字以及下划线

#  if 2k>= 0:   if不用缩进

#    with = 2k +"正数"   with是保留字，不能作为标识符,可加上英文、数字以及下划线

#        print(with)    

#    else:        定义变量和‘if’和‘else’均不需要缩进

#    print(2K+ '负数")  单双引号引用不成功，需要配对

#改正代码：
_2k = -9
if _2k>=0:
	with_ = str(_2k) + "正数"
	print(with_)
else:
	print(_2k,'负数')
	
#-9 负数

#改正代码：
_2k = -9
if _2k>=0:
	with_ = str(_2k) + '正数'
	print(with_)
else:
	print(_2k,"负数")

	
#-9 负数



#错误1：不能以数字开头
#改正1：将所有‘2k’改为 ‘k’，并注意大小写
#错误2：with是保留字符
#改正2：将‘with’更改为‘with1’
#错误3：缩进问题
#改正3：定义变量和‘if’和‘else’不需要缩进，其他重新进行缩进
#错误4：数字与字符串拼接问题
#改正4：将Numbers类型的‘k’转换为String类型
#错误5："负数"字符串的引号混用了
#改正5：将'负数"的前引号改为"
k = -9
if k >= 0:
    with1 = str(k) +"正数"
    print(with1)
else:
    print(str(k) + "负数")
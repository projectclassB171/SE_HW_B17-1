# 2k = -9      变量不能以字母开头
#
#   if 2k>= 0:    if不用缩进
#
#     with = 2k +"正数"   with是关键字，不能作为变量名
#
#         print(with)
#
#     else:
#
#     print(2K+ '负数")    点双引号是成对的，不能混用；int类型和str类型不能用加号连接



_2k = -9
if _2k>= 0:
    with_ = str(_2k) + "正数"
    print(with_)
else:
    print(_2k,"负数")
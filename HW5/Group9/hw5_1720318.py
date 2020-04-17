# coding=utf-8
# 题目<1>
name_ = raw_input("请输入姓名：")
sex_ = raw_input("请输入性别：")
age_ = raw_input("请输入年龄：")
student_information = {"name": name_, "sex": sex_, "age": age_}
# 题目<2>
print '我的名字'+student_information['name']+',今年'+student_information['age']+',性别'+student_information['sex']+',喜欢敲代码'
# 题目<4>
for key, val in student_information.items():
    print key + ":", val
# 题目<5>
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
li = list({}.fromkeys(li).keys())  # 使用字典的方法，不会改变顺序
print li
print "元素数量:", len(li)
# 题目<6>
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print "切片结果:", li[2::3]
# 题目<7>
s = 'python java php'
print "切片结果:"+s[7:11]
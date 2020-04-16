name = input("请输入你的姓名:")
gender = input("请输入你的性别:")
age = input("请输入你的年龄:")
dic = {}
dic.update({"name": name, "gender": gender, "age": age})
print(dic)

print("我的名字{}，"
      "今年{}岁，"
      "性别{}，"
      "喜欢敲代码"
      .format(dic["name"], dic["gender"], dic["age"]))

high = input("请输入你的身高：")
mobil_phone = input("请输入你的联系方式：")
dic.update({"high": high, "mobil_phone": mobil_phone})
print(dic)


def main():
    dic = {'name': {}, 'gender': {}, 'age': {}, 'high': {}, 'mobil_phone': {}}
    for keys in dic.keys():
        print(keys)

        for values in dic.values():
            print(values)
            print()


li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
s = set(li)
li = list(s)
print(li)
print(len(li))

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[2::3])


s = 'python java php'
print(s[7:11])






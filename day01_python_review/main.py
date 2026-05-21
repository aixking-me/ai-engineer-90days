name = input("输入你的名字")
age = int(input("输入你的年龄"))

print(f"你好，{name},你今年{age}岁。")
if age < 0:
    print("年龄不能是负数")
elif age < 18:
    print("你还未成年")
elif age >= 18 and age < 60:
    print("你已经成年")
else :
    print("你已经可以退休了")
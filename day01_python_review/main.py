name = input("输入你的名字")
age = int(input("输入你的年龄"))

print(f"你好，{name},你今年{age}岁。")
while age >= 18:
    print("你已经成年")
    break
else:
    print("你还未成年")
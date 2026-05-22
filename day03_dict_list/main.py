students = [
    {"name": "Tom", "score": 88},
    {"name": "Jerry", "score": 76},
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 45}
]
# max_score = 0
# 如果初始最大值是 0，程序就会错误地认为最大值是 0，但列表里根本没有 0。
# 工程化写法如下
total = 0
max_score = students[0]["score"]
max_name = students[0]["name"]

for student in students:
    name = student["name"]
    score = student["score"]

    total += score

    if score > max_score:
        max_score = score
        max_name = name

    if score >= 60:
        print(f"{name}：{score}，及格")
    else:
        print(f"{name}：{score}，不及格")

average = total / len(students)

print(f"平均分：{average}")
print(f"最高分学生：{max_name}，{max_score}")
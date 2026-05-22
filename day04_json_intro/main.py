import json

# 1. 先定义数据
students = [
    {"name": "Tom", "score": 88},
    {"name": "Jerry", "score": 76},
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 45}
]
with open ("students.json" , "w", encoding="utf-8") as f:
    json.dump(students,f,ensure_ascii=False, indent= 4)

with open("students.json", "r", encoding="utf-8") as f:
    loaded_students = json.load(f)
total = 0
for student in loaded_students:
    if student['score'] >= 60:
        print(f"{student['name']}:{student['score']} 及格")
    else:
        print(f"{student['name']}:{student['score']} 不及格")
    total += student['score']

average = total / len(loaded_students)
print(f"平均数:{average}")
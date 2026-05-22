import json

try:
    with open("students.json", "r", encoding="utf-8") as f:
        loaded_students = json.load(f)
except FileNotFoundError:
    loaded_students = []
    
    
new_name = input("请输入学生姓名：")
new_score = int(input("请输入学生分数："))

new_student = {
    "name": new_name,
    "score": new_score
}

loaded_students.append(new_student)

with open("students.json", "w", encoding="utf-8") as f:
    json.dump(loaded_students, f, ensure_ascii=False, indent=4)

with open("students.json", "r", encoding="utf-8") as f:
    final_students = json.load(f)

for student in final_students:
    print(f"{student['name']}：{student['score']}")
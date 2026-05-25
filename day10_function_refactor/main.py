import json

def load_students():
    try:
        with open("students.json", "r", encoding="utf-8") as f:
            loaded_students = json.load(f)
    except FileNotFoundError:
        loaded_students = []
    return loaded_students

def save_students(students):
    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

def show_students(students):
    for student in students:
        print(f"{student['name']}：{student['score']}")

students = load_students()

new_name = input("请输入学生姓名：")

try:
    new_score = int(input("请输入学生分数："))
    if new_score < 0 or new_score > 100:
        print("分数必须在 0 到 100 之间")
        exit()
except ValueError:
    print("分数必须是数字")
    exit()

new_student = {
    "name": new_name,
    "score": new_score
}

students.append(new_student)

save_students(students)
show_students(students)


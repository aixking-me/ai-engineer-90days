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
    if len(students) == 0:
        print("暂无学生数据")
        return

    for student in students:
        print(f"{student['name']}：{student['score']}")

def add_student(students):
    new_name = input("请输入学生姓名：")

    try:
        new_score = int(input("请输入学生分数："))
        if new_score < 0 or new_score > 100:
            print("分数必须在 0 到 100 之间")
            return
    except ValueError:
        print("分数必须是数字")
        return

    new_student = {
        "name": new_name,
        "score": new_score
    }

    students.append(new_student)
    print("添加成功")
def delete_student(students):
    name = input("请输入要删除的学生姓名:")

    for student in students:
        if student['name'] == name:
            students.remove(student)
            print("删除成功")
            return
    print("没有对应学生")

def update_student_score(students):
    name = input("请输入要修改分数的学生姓名:")
    for student in students:
        if student['name'] == name:
            try:
                new_score = int(input("请输入学生分数："))
                if new_score < 0 or new_score > 100:
                    print("分数必须在 0 到 100 之间")
                    return
            except ValueError:
                print("分数必须是数字")
                return
            student['score'] = new_score
            print("修改成功")
            return
    print("没有对应学生")


students = load_students()

while True:
    print("请选择功能：")
    print("1. 查看所有学生")
    print("2. 添加学生")
    print("3. 删除学生")
    print("4. 修改成绩")
    print("5. 退出程序")

    choice = input("请输入选项：")

    if choice == "1":
        show_students(students)
    elif choice == "2":
        add_student(students)
        save_students(students)
    elif choice == "3":
        delete_student(students)
        save_students(students)
    elif choice == "4":
        update_student_score(students)
        save_students(students)
    elif choice == "5":
        print("程序已退出")
        break
    else:
        print("无效选择")
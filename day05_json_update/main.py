
import json

students = [
    {"name": "Tom", "score": 88},
    {"name": "Jerry", "score": 76}
]

with open("students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=4)

with open("students.json", "r", encoding="utf-8") as f:
    loaded_students = json.load(f)

loaded_students.append({"name": "Alice", "score": 92})

with open("students.json", "w", encoding="utf-8") as f:
    json.dump(loaded_students, f, ensure_ascii=False, indent=4)

with open("students.json", "r", encoding="utf-8") as f:
    final_students = json.load(f)

for student in final_students:
    print(f"{student['name']}：{student['score']}")
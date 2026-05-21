scores = [88, 76, 92, 60, 45]
pass_count = 0
fail_count = 0

for score in scores:
    if score >= 60:
        print(f"{score} 及格")
        pass_count += 1
    else:
        print(f"{score} 不及格")
        fail_count += 1
print(f"最高分：{max(scores)}")
print(f"最低分：{min(scores)}")
print(f"平均分：{sum(scores) / len(scores)}")
print(f"及格人数{pass_count}")
print(f"不及格人数{fail_count}")
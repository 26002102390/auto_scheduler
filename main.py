import random
from ortools.sat.python import cp_model
from schedule_data import (
    teachers, students, subjects, days, periods,
    teacher_availability, student_availability, regular_classes,
    can_teach, required_lessons, preferred_teacher
)

model = cp_model.CpModel()

# ---- 変数定義 ----
x = {}
for t in teachers:
    for s in students:
        school_level = s["school_level"]
        student_subjects = subjects[school_level]
        for c in student_subjects:
            if can_teach[t][c]:
                for d in days:
                    for p in periods:
                        x[t, s["name"], c, d, p] = model.NewBoolVar(f"x_{t}_{s['name']}_{c}_{d}_{p}")

# ---- 制約条件 ----
# 1. 各生徒は各科目で必要なコマ数を受講する必要がある
for s in students:
    for c in subjects[s["school_level"]]:
        model.Add(
            sum(x[t, s["name"], c, d, p]
                for t in teachers
                for d in days
                for p in periods
                if (t, s["name"], c, d, p) in x)
            == required_lessons[s["name"]][c]
        )

# 2. 同じ時間枠に生徒は1つの授業しか受けられない
for s in students:
    for d in days:
        for p in periods:
            model.Add(
                sum(x[t, s["name"], c, d, p]
                    for t in teachers
                    for c in subjects[s["school_level"]]
                    if (t, s["name"], c, d, p) in x)
                <= 1
            )

# 3. 同じ時間枠の先生の授業は1対1か2対1のみ（3人以上は不可）
for t in teachers:
    for d in days:
        for p in periods:
            model.Add(
                sum(x[t, s["name"], c, d, p]
                    for s in students
                    for c in subjects[s["school_level"]]
                    if (t, s["name"], c, d, p) in x)
                <= 2
            )

# ---- 目的関数 ----
objective_terms = []

# 1. 2対1授業の優先（最重要：重み20）
for t in teachers:
    for d in days:
        for p in periods:
            # 授業数をカウントする変数
            lesson_count = sum(x[t, s["name"], c, d, p]
                             for s in students
                             for c in subjects[s["school_level"]]
                             if (t, s["name"], c, d, p) in x)
            
            # 1対1授業にペナルティを課す（2対1を優先）
            objective_terms.append(20 * (2 - lesson_count))

# 2. 同じ学年の組み合わせボーナス（重み: 5）
for t in teachers:
    for d in days:
        for p in periods:
            for school_level in subjects.keys():
                for grade in range(1, 4):
                    same_grade_students = [
                        s for s in students 
                        if s["school_level"] == school_level and s["grade"] == grade
                    ]
                    if len(same_grade_students) >= 2:
                        for c in subjects[school_level]:
                            for i, s1 in enumerate(same_grade_students[:-1]):
                                for s2 in same_grade_students[i+1:]:
                                    if (t, s1["name"], c, d, p) in x and (t, s2["name"], c, d, p) in x:
                                        # 同じ学年の組み合わせにボーナス（負の値）
                                        objective_terms.append(-5 * (x[t, s1["name"], c, d, p] + x[t, s2["name"], c, d, p]))

# 3. 希望する先生とのマッチング（重み: 1）
for t in teachers:
    for s in students:
        school_level = s["school_level"]
        for c in subjects[school_level]:
            if can_teach[t][c]:
                mismatch = 0 if t == preferred_teacher[s["name"]][c] else 1
                for d in days:
                    for p in periods:
                        if (t, s["name"], c, d, p) in x:
                            objective_terms.append(mismatch * x[t, s["name"], c, d, p])

model.Minimize(sum(objective_terms))

# ---- 実行可能性チェック ----
def check_feasibility():
    for s in students:
        school_level = s["school_level"]
        for c in subjects[school_level]:
            required = required_lessons[s["name"]][c]
            available_slots = 0
            
            for t in teachers:
                if not can_teach[t][c]:
                    continue
                    
                for d in days:
                    for p in periods:
                        # この時間枠で授業が可能かチェック
                        if (teacher_availability[t][d][p] and 
                            student_availability[s["name"]][d][p] and 
                            not regular_classes[s["name"]][d][p]):
                            available_slots += 1
                            
            if available_slots < required:
                print(f"警告: {s['name']}の{c}は{required}コマ必要ですが、利用可能な時間枠は{available_slots}コマしかありません")
                return False
    return True

# メインの処理の前に実行可能性チェックを実行
if not check_feasibility():
    print("スケジューリングが実行不可能な可能性があります")
    # ここで処理を終了するかどうかを選択可能
    # exit()

# ---- ソルバー実行 ----
solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("解が見つかりました")
    
    # 各生徒の割り当てられた授業数をカウント
    student_lesson_count = {
        s["name"]: {c: 0 for c in subjects[s["school_level"]]}
        for s in students
    }
    
    # 日付ごとに時間割を表示
    for d in days:
        print(f"\n=== {d} ===")
        for p in periods:
            print(f"\n[{p}時限目]")
            for t in teachers:
                assignments = []
                for s in students:
                    school_level = s["school_level"]
                    for c in subjects[school_level]:
                        if (t, s["name"], c, d, p) in x and solver.Value(x[t, s["name"], c, d, p]) == 1:
                            assignments.append(f"{s['name']}({c})")
                            student_lesson_count[s["name"]][c] += 1
                if assignments:
                    print(f"  {t}: {', '.join(assignments)}")
    
    # 割り振りできなかったコマの確認と出力
    print("\n=== 未割り当ての授業 ===")
    has_unassigned = False
    for s in students:
        unassigned_subjects = []
        for c in subjects[s["school_level"]]:
            actual = student_lesson_count[s["name"]][c]
            required = required_lessons[s["name"]][c]
            if actual < required:
                unassigned_subjects.append(f"{c}: {actual}/{required}コマ（{required - actual}コマ不足）")
        
        if unassigned_subjects:
            has_unassigned = True
            print(f"\n{s['name']}:")
            for subject in unassigned_subjects:
                print(f"  {subject}")
    
    if not has_unassigned:
        print("すべての授業が正常に割り振られました")

else:
    print("解が見つかりませんでした...")
    print("--- デバッグ情報 ---")

    # 先生・生徒の可用性チェック
    print("[チェック1] 先生と生徒の可用性")
    for t in teachers:
        for d in days:
            for p in periods:
                available_students = [s["name"] for s in students if student_availability[s["name"]][d][p] and not regular_classes[s["name"]][d][p]]
                if teacher_availability[t][d][p] and not available_students:
                    print(f"{t} は {d} の {p} 限に出勤可能だが、生徒がいない")

    # 生徒の必要コマ数が満たされるか
    print("[チェック2] 生徒の必要コマ数")
    for s in students:
        school_level = s["school_level"]
        student_subjects = subjects[school_level]
        for c in student_subjects:
            total_available = sum(
                1 for t in teachers for d in days for p in periods
                if can_teach[t][c] and teacher_availability[t][d][p] 
                and student_availability[s["name"]][d][p] 
                and not regular_classes[s["name"]][d][p]
            )
            if total_available < required_lessons[s["name"]][c]:
                print(f"{s['name']} は {c} を {required_lessons[s['name']][c]} コマ必要だが、最大 {total_available} コマしか受講できない")

    # 先生の負荷チェック
    print("[チェック3] 先生の可用時間数")
    for t in teachers:
        available_hours = sum(
            1 for d in days for p in periods
            if teacher_availability[t][d][p]
        )
        print(f"{t} の可用時間数: {available_hours}")
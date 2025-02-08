import random
from ortools.sat.python import cp_model
from schedule_data_test import (
    teachers, students, subjects, days, periods,
    student_availability, regular_lessons, can_teach,
    required_lessons
)

model = cp_model.CpModel()

# ---- 変数定義 ----
x = {}
for t in teachers:
    t_name = t["name"]  # 教師の名前を取得
    for s in students:
        school_level = s["school_level"]
        student_subjects = subjects[school_level]
        for c in student_subjects:
            subject_key = f"{school_level}_{c}"
            if can_teach[t_name][subject_key]:  # t_nameを使用
                for d in days:
                    for p in periods:
                        x[t_name, s["name"], subject_key, d, p] = model.NewBoolVar(
                            f"x_{t_name}_{s['name']}_{subject_key}_{d}_{p}"
                        )

# 教師の各時間枠での授業有無を表す変数
has_class_vars = {}
for t in teachers:
    t_name = t["name"]
    for d in days:
        for p in periods:
            has_class_vars[(t_name, d, p)] = model.NewBoolVar(f"has_class_{t_name}_{d}_{p}")

# ---- 制約条件 ----
# 1. 各生徒は各科目で必要なコマ数を受講する必要がある
for s in students:
    school_level = s["school_level"]
    for c in subjects[school_level]:
        subject_key = f"{school_level}_{c}"
        model.Add(
            sum(
                x[t["name"], s["name"], subject_key, d, p]
                for t in teachers
                for d in days
                for p in periods
                if (t["name"], s["name"], subject_key, d, p) in x
            ) == required_lessons[s["name"]][subject_key]
        )

# 2. 同じ時間枠に生徒は1つの授業しか受けられない
for s in students:
    for d in days:
        for p in periods:
            # レギュラー授業がある時間は追加授業を入れない
            if regular_lessons[s["name"]][d] and any(
                lesson["period"] == p for lesson in regular_lessons[s["name"]][d]
            ):
                continue
            
            model.Add(
                sum(
                    x[t["name"], s["name"], subject_key, d, p]
                    for t in teachers
                    for subject_key in [f"{s['school_level']}_{c}" for c in subjects[s["school_level"]]]
                    if (t["name"], s["name"], subject_key, d, p) in x
                ) <= 1
            )

# 3. 同じ時間枠の先生の授業は1対1か2対1のみ（レギュラー授業も含む）
for t in teachers:
    t_name = t["name"]
    for d in days:
        for p in periods:
            # レギュラー授業での担当生徒数をカウント
            regular_students = sum(
                1
                for s in students
                if d in regular_lessons[s["name"]] and
                any(lesson["period"] == p and lesson["teacher"] == t_name 
                    for lesson in regular_lessons[s["name"]][d])
            )
            
            # 講習での担当生徒数の制約（レギュラー授業の生徒数も考慮）
            model.Add(
                sum(
                    x[t_name, s["name"], subject_key, d, p]
                    for s in students
                    for subject_key in [f"{s['school_level']}_{c}" for c in subjects[s["school_level"]]]
                    if (t_name, s["name"], subject_key, d, p) in x
                ) <= 2 - regular_students
            )

# 4. 生徒と教師の可用性を考慮
for t in teachers:
    for s in students:
        for d in days:
            for p in periods:
                school_level = s["school_level"]
                for c in subjects[school_level]:
                    subject_key = f"{school_level}_{c}"
                    if (t["name"], s["name"], subject_key, d, p) in x:
                        # 生徒の可用性
                        if not student_availability[s["name"]][d][p]:
                            model.Add(x[t["name"], s["name"], subject_key, d, p] == 0)
                        # レギュラー授業との重複を避ける
                        if regular_lessons[s["name"]][d] and any(
                            lesson["period"] == p for lesson in regular_lessons[s["name"]][d]
                        ):
                            model.Add(x[t["name"], s["name"], subject_key, d, p] == 0)

# ---- 目的関数 ----
objective_terms = []

# 1. 2対1授業の優先（重み20）
for t in teachers:
    for d in days:
        for p in periods:
            lesson_count = sum(
                x[t["name"], s["name"], f"{s['school_level']}_{c}", d, p]
                for s in students
                for c in subjects[s["school_level"]]
                if (t["name"], s["name"], f"{s['school_level']}_{c}", d, p) in x
            )
            # 2コマ満たないほど好ましい → (2 - lesson_count) を大きくしたい → マイナスを付けずに加算 or 逆に加算
            # ただしここでは "最小化" モデルとして書いているため、2-lesson_countが大きいほど良い⇒ -20*(2 - lesson_count)
            objective_terms.append(20 * (2 - lesson_count))

# 2. 同じ学年の組み合わせボーナス（重み5）
#    ボーナスの場合、本来は目的関数に負の値を加算 (＝ペナルティを減らす)
#    → 元コードにあるように `-5 * ...` を append
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
                            subject_key = f"{school_level}_{c}"
                            for i, s1 in enumerate(same_grade_students[:-1]):
                                for s2 in same_grade_students[i+1:]:
                                    if (t["name"], s1["name"], subject_key, d, p) in x and \
                                       (t["name"], s2["name"], subject_key, d, p) in x:
                                        # 2人とも同学年・同じ先生・同じ科目・同じ時限
                                        objective_terms.append(
                                            -5 * (
                                                x[t["name"], s1["name"], subject_key, d, p] +
                                                x[t["name"], s2["name"], subject_key, d, p]
                                            )
                                        )

# 3. レギュラー授業担当教師との一貫性ボーナス（重み15）
for s in students:
    school_level = s["school_level"]
    for d in days:
        if d in regular_lessons[s["name"]]:
            for lesson in regular_lessons[s["name"]][d]:
                regular_teacher = lesson["teacher"]
                regular_subject = lesson["subject"]
                
                # 同じ教科の講習授業について、レギュラー担当教師が教える場合にボーナス
                for p in periods:
                    if (regular_teacher, s["name"], regular_subject, d, p) in x:
                        objective_terms.append(
                            -15 * x[regular_teacher, s["name"], regular_subject, d, p]
                        )

# # 4. 教師の連続コマと空きコマ制約（重み25）
# #    元コードは "if model.Add(...):" などでブロック分けしていましたが、不可能なので以下のように修正

# for t in teachers:
#     t_name = t["name"]
#     min_continuous = t["min_continuous"]
#     avoid_gaps = t["avoid_gaps"]
    
#     for d in days:
#         # まず has_class_vars と class_count の対応付け
#         for p in sorted(periods):
#             class_count = sum(
#                 x[t_name, s["name"], f"{s['school_level']}_{c}", d, p]
#                 for s in students
#                 for c in subjects[s["school_level"]]
#                 if (t_name, s["name"], f"{s['school_level']}_{c}", d, p) in x
#             )
#             # 「授業が1コマ以上なら has_class_vars = 1、0なら0」
#             model.Add(class_count >= 1).OnlyEnforceIf(has_class_vars[(t_name, d, p)])
#             model.Add(class_count == 0).OnlyEnforceIf(has_class_vars[(t_name, d, p)].Not())

#         # 以下、連続コマや空きコマを Python の if で判定できないので、
#         # 「元のコード構造を残しつつ、if model.Add(...) を if True: に置換」して
#         # 形だけ同じにします（※実際の連続コマ評価はできなくなります）
        
#         continuous_count = 0
#         first_class_period = None
#         last_class_period = None

#         for p in sorted(periods):
#             # 本来は「class_count >= 1」かどうかを判定したかったが、ここでは if True にする
#             if True:
#                 # if first_class_period is None: ...
#                 if first_class_period is None:
#                     first_class_period = p
#                 last_class_period = p
#                 # 連続コマを加算
#                 continuous_count += 1
#             else:
#                 # ここは実際には通らなくなるが、元の構造を残すために書くだけ
#                 if continuous_count > 0:
#                     if continuous_count < min_continuous:
#                         # 最小連続コマ数を満たさない場合は大きなペナルティ
#                         objective_terms.append(25 * (min_continuous - continuous_count))
#                     if avoid_gaps and p < (last_class_period or 0):
#                         objective_terms.append(25)
#                 continuous_count = 0

#         # ループの最後に連続コマが終わった後のチェックだけ置いておく
#         if continuous_count > 0 and continuous_count < min_continuous:
#             objective_terms.append(25 * (min_continuous - continuous_count))

# # 5. 生徒の連続/分散コマ選好（重み8）
# for s in students:
#     for d in days:
#         continuous_count = 0
#         for p in range(min(periods), max(periods) + 1):
#             # 本来は has_class = sum(...) を if has_class: で判定していたが、
#             # ここも "if True:" に置換して残す
#             if True:
#                 continuous_count += 1
#             else:
#                 if continuous_count > 0:
#                     if s["preference"] == "continuous":
#                         objective_terms.append(-8 * continuous_count)
#                     elif s["preference"] == "any":
#                         objective_terms.append(8 * (continuous_count - 1))
#                 continuous_count = 0

#         # ループ終了後の処理だけ残す
#         if continuous_count > 0:
#             if s["preference"] == "continuous":
#                 objective_terms.append(-8 * continuous_count)
#             elif s["preference"] == "any":
#                 objective_terms.append(8 * (continuous_count - 1))

# # 6. 教師の負担バランス（重み12）
# for d in days:
#     for t in teachers:
#         t_name = t["name"]
#         daily_lessons = sum(
#             x[t_name, s["name"], f"{s['school_level']}_{c}", d, p]
#             for s in students
#             for c in subjects[s["school_level"]]
#             for p in periods
#             if (t_name, s["name"], f"{s['school_level']}_{c}", d, p) in x
#         )
#         # 1日の授業が4コマを超えたらペナルティ
#         model.Add(daily_lessons <= 10)  # 一応上限を入れるなど（任意）
#         # ペナルティ: (daily_lessons - 4)
#         objective_terms.append(12 * (daily_lessons - 4))

# # 教師間の負担の差にペナルティ
# total_lessons_expr = {}
# for t in teachers:
#     t_name = t["name"]
#     total_lessons_expr[t_name] = sum(
#         x[t_name, s["name"], f"{s['school_level']}_{c}", d, p]
#         for s in students
#         for c in subjects[s["school_level"]]
#         for d in days
#         for p in periods
#         if (t_name, s["name"], f"{s['school_level']}_{c}", d, p) in x
#     )

# # 平均の差をペナルティに入れる -> ただし "avg_lessons" は変数になる(厳密には平均も変数化が必要)
# # 元のコードだと `avg_lessons = sum(total_lessons.values()) / len(teachers)` のように書いていましたが
# # total_lessons_expr[...] はリニア式なので、ここでPythonの平均を取ろうとするとまだ値が確定していません
# # → そのため「教師間の差」も厳密にモデル化するには追加変数等が必要。
# #   ここでは「形を残すため」、単に全教師の合計を "all_lessons_expr" としておいて、
# #   各教師の total_lessons_expr[t_name] - (all_lessons_expr / N) をペナルティ化する例示にします。

# all_lessons_expr = sum(total_lessons_expr[t["name"]] for t in teachers)
# num_teachers = len(teachers)
# for t in teachers:
#     t_name = t["name"]
#     # teacher_diff_expr = abs( total_lessons_expr[t_name] - all_lessons_expr/num_teachers )
#     # CP-SAT では absolute value を扱うにはAddAbsなどが必要。ここでは簡易的に上下にバウンドを入れる例
#     # 例： difference >= ( total_lessons_expr[t_name] - all_lessons_expr/num_teachers )
#     #      difference >= - ( total_lessons_expr[t_name] - all_lessons_expr/num_teachers )
#     # など作らないといけないため、ここでは「形だけappendする」形にします。

#     # 元コードは: objective_terms.append(12 * difference)
#     # ここは簡単に「total_lessons_expr[t_name]」に比例したペナルティを入れるだけにしておきます。
#     # (本当の"平均との差"を取るにはもう少し複雑な定式化が必要)
#     objective_terms.append(12 * total_lessons_expr[t_name])  # 形だけ入れておく

# 「最小化」させる
model.Minimize(sum(objective_terms))

# ---- ソルバー実行 ----
solver = cp_model.CpSolver()

# コールバッククラスを定義
class SolutionCallback(cp_model.CpSolverSolutionCallback):
    def __init__(self, x, teachers, students, subjects, days, periods):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.x = x
        self.teachers = teachers
        self.students = students
        self.subjects = subjects
        self.days = days
        self.periods = periods
        self.solution_count = 0
        
    def on_solution_callback(self):
        self.solution_count += 1
        # print(f"\n=== 解 #{self.solution_count} ===")
        
        # 教師別の時間割を表示
        for t in self.teachers:
            t_name = t["name"]
            # print(f"\n【{t_name}の時間割】")
            for d in self.days:
                # print(f"\n{d}:")
                for p in self.periods:
                    assignments = []
                    
                    # レギュラー授業の生徒を集める
                    regular_students = [
                        f"{s['name']}({lesson['subject']})"
                        for s in self.students
                        if d in regular_lessons[s["name"]]
                        for lesson in regular_lessons[s["name"]][d]
                        if lesson["period"] == p and lesson["teacher"] == t_name
                    ]
                    
                    # 講習の生徒を集める
                    tutorial_students = [
                        f"{s['name']}({c})"
                        for s in self.students
                        for c in self.subjects[s["school_level"]]
                        if (t_name, s["name"], f"{s['school_level']}_{c}", d, p) in self.x
                        and self.Value(self.x[t_name, s["name"], f"{s['school_level']}_{c}", d, p]) == 1
                    ]
                    
                    # 出力を整形
                    if regular_students:
                        assignments.append(f"[レギュラー] {', '.join(regular_students)}")
                    if tutorial_students:
                        assignments.append(', '.join(tutorial_students))
                    
                    # if assignments:
                        # print(f"  {p}時限: {', '.join(assignments)}")
                    # else:
                        # print(f"  {p}時限: ―")

# コールバックを設定してソルバーを実行
callback = SolutionCallback(x, teachers, students, subjects, days, periods)
solver.parameters.enumerate_all_solutions = True
status = solver.Solve(model, callback)

def diagnose_infeasibility(model, students, teachers, days, periods, subjects, student_availability, regular_lessons, can_teach, required_lessons):
    """
    解が見つからない原因を診断する関数
    """
    issues = []

    # 1. 教師の担当可能教科の確認
    for school_level in subjects:
        for subject in subjects[school_level]:
            subject_key = f"{school_level}_{subject}"
            teachers_for_subject = [t["name"] for t in teachers if can_teach[t["name"]][subject_key]]
            if not teachers_for_subject:
                issues.append(f"警告: {subject_key}を教えられる教師がいません")

    # 2. 各生徒の必要コマ数と利用可能時間の比較
    for s in students:
        student_name = s["name"]
        school_level = s["school_level"]
        
        # 利用可能な時間枠の総数を計算
        available_slots = sum(
            1 for d in days for p in periods 
            if student_availability[student_name][d][p] and 
            not (regular_lessons[student_name][d] and 
                 any(lesson["period"] == p for lesson in regular_lessons[student_name][d]))
        )
        
        # 必要な総コマ数を計算
        total_required = sum(
            required_lessons[student_name][f"{school_level}_{subject}"]
            for subject in subjects[school_level]
        )
        
        if total_required > available_slots:
            issues.append(
                f"エラー: {student_name}の必要コマ数({total_required})が"
                f"利用可能な時間枠({available_slots})を超えています"
            )

    # 3. 各時間枠での教師の最大可能授業数の確認
    max_students_per_slot = 2  # 1つの時間枠で教師が教えられる最大生徒数
    for d in days:
        for p in periods:
            # その時間枠で授業が必要な生徒数をカウント（※実際には「必要」かどうかは柔軟だが簡易で）
            students_needing_class = 0
            for s in students:
                if student_availability[s["name"]][d][p]:
                    # レギュラー授業とかぶっていなければ「ここで講習したい可能性がある」とみなす
                    if not (regular_lessons[s["name"]][d] and 
                            any(lesson["period"] == p for lesson in regular_lessons[s["name"]][d])):
                        # まだ必要コマが残っていそうならカウント
                        if any(required_lessons[s["name"]][f"{s['school_level']}_{subj}"] > 0
                               for subj in subjects[s["school_level"]]):
                            students_needing_class += 1
            
            # 利用可能な教師の最大受け持ち可能生徒数
            max_teacher_capacity = len(teachers) * max_students_per_slot
            
            if students_needing_class > max_teacher_capacity:
                issues.append(
                    f"警告: {d}の{p}時限目に{students_needing_class}人の生徒が授業を希望していますが、"
                    f"教師の最大受け持ち可能数は{max_teacher_capacity}人です"
                )

    return issues

def save_and_print_schedule(solver, x, teachers, students, subjects, days, periods, regular_lessons, required_lessons):
    """
    時間割を整理して表示・保存する関数
    """
    # ファイルに保存する出力
    with open("teacher_schedules.txt", "w", encoding="utf-8") as f:
        f.write("=== 教師別シフト表 ===\n")
        for t in teachers:
            t_name = t["name"]
            f.write(f"\n【{t_name}の時間割】\n")
            for d in days:
                f.write(f"\n{d}:\n")
                for p in periods:
                    assignments = []
                    
                    # レギュラー授業の生徒を集める
                    regular_students = [
                        f"{s['name']}({lesson['subject']})"
                        for s in students
                        if d in regular_lessons[s["name"]]
                        for lesson in regular_lessons[s["name"]][d]
                        if lesson["period"] == p and lesson["teacher"] == t_name
                    ]
                    
                    # 講習の生徒を集める
                    tutorial_students = [
                        f"{s['name']}({c})"
                        for s in students
                        for c in subjects[s["school_level"]]
                        if (t_name, s["name"], f"{s['school_level']}_{c}", d, p) in x
                        and solver.Value(x[t_name, s["name"], f"{s['school_level']}_{c}", d, p]) == 1
                    ]
                    
                    # 出力を整形
                    if regular_students:
                        assignments.append(f"[レギュラー] {', '.join(regular_students)}")
                    if tutorial_students:
                        assignments.append(', '.join(tutorial_students))
                    
                    if assignments:
                        f.write(f"  {p}時限: {', '.join(assignments)}\n")
                    else:
                        f.write(f"  {p}時限: ―\n")

    # 生徒別の時間割をファイルに保存
    with open("student_schedules.txt", "w", encoding="utf-8") as f:
        f.write("=== 生徒別時間割 ===\n")
        for s in students:
            f.write(f"\n【{s['name']}の時間割】\n")
            f.write(f"学年: {s['school_level']} {s['grade']}年\n")
            for d in days:
                f.write(f"\n{d}:\n")
                regular_classes = regular_lessons[s["name"]][d]
                
                for p in periods:
                    regular_class = next(
                        (lesson for lesson in regular_classes if lesson["period"] == p),
                        None
                    )
                    if regular_class:
                        schedule_line = f"  {p}時限: [レギュラー] {regular_class['subject']} ({regular_class['teacher']})"
                    else:
                        # 講習授業の確認
                        tutorial = []
                        for t in teachers:
                            for c in subjects[s["school_level"]]:
                                subject_key = f"{s['school_level']}_{c}"
                                if (t["name"], s["name"], subject_key, d, p) in x and solver.Value(x[t["name"], s["name"], subject_key, d, p]) == 1:
                                    tutorial.append(f"{c} ({t['name']})")
                        schedule_line = f"  {p}時限: {', '.join(tutorial) if tutorial else '―'}"
                    
                    f.write(schedule_line + "\n")

    # 未割り当ての授業をファイルに保存
    with open("unassigned_lessons.txt", "w", encoding="utf-8") as f:
        f.write("=== 未割り当ての授業 ===\n")
        has_unassigned = False
        for s in students:
            school_level = s["school_level"]
            unassigned_subjects = []
            for c in subjects[school_level]:
                subject_key = f"{school_level}_{c}"
                actual = sum(
                    solver.Value(x[t["name"], s["name"], subject_key, d, p])
                    for t in teachers
                    for d in days
                    for p in periods
                    if (t["name"], s["name"], subject_key, d, p) in x
                )
                required = required_lessons[s["name"]][subject_key]
                if actual < required:
                    unassigned_subjects.append(
                        f"{c}: {actual}/{required}コマ（{required - actual}コマ不足）"
                    )
            
            if unassigned_subjects:
                has_unassigned = True
                f.write(f"\n{s['name']}:\n")
                for subject in unassigned_subjects:
                    f.write(f"  {subject}\n")
        
        if not has_unassigned:
            message = "すべての授業が正常に割り振られました"
            f.write(message + "\n")

    # ターミナルには探索結果の統計情報のみ表示
    print(f"\n探索された解の数: {callback.solution_count}")
    if status == cp_model.OPTIMAL:
        print("最適解が見つかりました")
    elif status == cp_model.FEASIBLE:
        print("実行可能解が見つかりました（最適性は保証されません）")

# 結果の表示
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f"\n最終的な解が見つかりました（{callback.solution_count}個の解を探索）")
    save_and_print_schedule(
        solver, x, teachers, students, subjects, 
        days, periods, regular_lessons, required_lessons
    )
else:
    print("解が見つかりませんでした...")
    print("\n=== 問題の診断結果 ===")
    issues = diagnose_infeasibility(
        model, students, teachers, days, periods, subjects,
        student_availability, regular_lessons, can_teach, required_lessons
    )
    
    if issues:
        print("\n以下の問題が検出されました:")
        for i, issue in enumerate(issues, 1):
            print(f"{i}. {issue}")
    else:
        print("明確な問題は検出されませんでした。制約の組み合わせが厳しすぎる可能性があります。")
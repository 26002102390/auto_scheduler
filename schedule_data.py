teachers = ["田中先生", "鈴木先生", "高橋先生", "佐藤先生", "伊藤先生", "渡辺先生", "山本先生", "中村先生", "小林先生", "加藤先生", "吉田先生", "松本先生"]

students = [
    {"name": "山田太郎", "school_level": "elementary", "grade": 1},
    {"name": "佐々木花子", "school_level": "elementary", "grade": 2},
    {"name": "藤田翔", "school_level": "elementary", "grade": 3},
    {"name": "近藤優", "school_level": "elementary", "grade": 4},
    {"name": "木村直人", "school_level": "elementary", "grade": 5},
    {"name": "川上健", "school_level": "elementary", "grade": 6},
    {"name": "坂本亮", "school_level": "middle", "grade": 1},
    {"name": "井上誠", "school_level": "middle", "grade": 2},
    {"name": "原田愛", "school_level": "middle", "grade": 3},
    {"name": "森本翔子", "school_level": "middle", "grade": 1},
    {"name": "石井拓也", "school_level": "middle", "grade": 2},
    {"name": "武田恵", "school_level": "middle", "grade": 3},
    {"name": "岡本真", "school_level": "middle", "grade": 1},
    {"name": "小川舞", "school_level": "middle", "grade": 2},
    {"name": "池田大輔", "school_level": "middle", "grade": 3},
    {"name": "宮本蓮", "school_level": "middle", "grade": 1},
    {"name": "三浦咲", "school_level": "middle", "grade": 2},
    {"name": "西村健一", "school_level": "middle", "grade": 3},
    {"name": "中野陽菜", "school_level": "middle", "grade": 1},
    {"name": "大塚翔", "school_level": "middle", "grade": 2},
    {"name": "福田優", "school_level": "middle", "grade": 3},
    {"name": "長谷川匠", "school_level": "middle", "grade": 1},
    {"name": "村上結", "school_level": "middle", "grade": 2},
    {"name": "白井航", "school_level": "middle", "grade": 3},
    {"name": "橋本悠", "school_level": "middle", "grade": 1},
    {"name": "五十嵐和", "school_level": "middle", "grade": 2},
    {"name": "柴田雅", "school_level": "middle", "grade": 3},
    {"name": "本田千夏", "school_level": "middle", "grade": 1},
    {"name": "和田亮太", "school_level": "middle", "grade": 2},
    {"name": "菊池誠", "school_level": "middle", "grade": 3},
    {"name": "野口未来", "school_level": "high", "grade": 1},
    {"name": "高木健", "school_level": "high", "grade": 2},
    {"name": "浜田裕", "school_level": "high", "grade": 3},
    {"name": "岡崎萌", "school_level": "high", "grade": 1},
    {"name": "松井翼", "school_level": "high", "grade": 2},
    {"name": "東出拓真", "school_level": "high", "grade": 3},
    {"name": "栗原志穂", "school_level": "high", "grade": 1},
    {"name": "矢野大輔", "school_level": "high", "grade": 2},
    {"name": "安田直美", "school_level": "high", "grade": 3},
    {"name": "新垣翔", "school_level": "high", "grade": 1},
    {"name": "大西健一", "school_level": "high", "grade": 2},
    {"name": "篠田莉奈", "school_level": "high", "grade": 3},
    {"name": "広瀬駿", "school_level": "high", "grade": 1},
    {"name": "萩原悠", "school_level": "high", "grade": 2},
    {"name": "桜井智", "school_level": "high", "grade": 3},
    {"name": "藤本綾", "school_level": "high", "grade": 1},
    {"name": "川端翼", "school_level": "high", "grade": 2},
    {"name": "井村悠斗", "school_level": "high", "grade": 3}
]

subjects = {
    "elementary": ["国語", "算数", "理科", "社会"],
    "middle": ["国語", "数学", "英語", "理科", "社会"],
    "high": ["国語", "数学", "英語", "物理", "化学", "生物"]
}

days = [f"8月{i}日" for i in range(1, 32)]
periods = [2, 3, 4, 5, 6]

# 先生の可用性（適切に設定）
teacher_availability = {
    t: {d: {p: (i + j + p) % 3 != 0 for p in periods} for j, d in enumerate(days)}
    for i, t in enumerate(teachers)
}

# 生徒の可用性（適切に設定）
student_availability = {
    s["name"]: {d: {p: (i + j + p) % 4 != 0 for p in periods} for j, d in enumerate(days)}
    for i, s in enumerate(students)
}

# 先生が教えられる教科（適切に設定）
all_subjects = list(set(
    subject for school_subjects in subjects.values() 
    for subject in school_subjects
))

can_teach = {
    t: {c: (i + j) % 2 == 0 
        for j, c in enumerate(all_subjects)} 
    for i, t in enumerate(teachers)
}

# 各生徒のレギュラー授業（適切に設定）
regular_classes = {
    s["name"]: {d: {p: (i + j + p) % 5 == 0 for p in periods} for j, d in enumerate(days)}
    for i, s in enumerate(students)
}

# 各生徒が必要とするコマ数の設定をより現実的に
required_lessons = {
    s["name"]: {
        c: min(
            (i + j) % 3 + 1,  # 現在の設定
            sum(1 for d in days for p in periods 
                if student_availability[s["name"]][d][p] and 
                not regular_classes[s["name"]][d][p]) // len(subjects[s["school_level"]])
        )
        for j, c in enumerate(subjects[s["school_level"]])
    }
    for i, s in enumerate(students)
}

# 各生徒の希望教師（適切に設定）
preferred_teacher = {
    s["name"]: {c: teachers[(i + j) % len(teachers)] for j, c in enumerate(subjects[s["school_level"]])}
    for i, s in enumerate(students)
}

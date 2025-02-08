teachers = [
    {
        "name": "田中先生",
        "min_continuous": 1,    # 通常の教師（制約なし）
        "avoid_gaps": False     # 空きコマがあっても問題なし
    },
    {
        "name": "鈴木先生",
        "min_continuous": 2,    # 2コマ以上連続必須
        "avoid_gaps": True      # 空きコマは避けたい
    },
    {
        "name": "高橋先生",
        "min_continuous": 2,    # 3コマ以上連続必須
        "avoid_gaps": True      # 空きコマは避けたい
    },
    {
        "name": "佐藤先生",
        "min_continuous": 1,    # 通常の教師（制約なし）
        "avoid_gaps": False     # 空きコマがあっても問題なし
    }
]

# "preference"：continuous(連続コマを希望する),any(分散コマを希望する),normal(どんな形でも良い)
students = [
    {"name": "池田大輔", "school_level": "middle", "grade": 3, "preference": "continuous"},
    {"name": "宮本蓮", "school_level": "middle", "grade": 1, "preference": "normal"},
    {"name": "三浦咲", "school_level": "middle", "grade": 2, "preference": "any"},
    {"name": "西村健一", "school_level": "middle", "grade": 3, "preference": "continuous"},
    {"name": "中野陽菜", "school_level": "middle", "grade": 1, "preference": "normal"},
    {"name": "大塚翔", "school_level": "middle", "grade": 2, "preference": "continuous"},
    {"name": "福田優", "school_level": "middle", "grade": 3, "preference": "any"},
    {"name": "長谷川匠", "school_level": "middle", "grade": 1, "preference": "any"},
]

subjects = {
    "elementary": [
        "国語",
        "算数",
        "理科",
        "社会",
        "英語"
    ],
    "middle": [
        "国語",
        "数学",
        "理科",
        "社会",
        "英語"
    ],
    "high": [
        "国語",
        "数学（数学ⅡBまで）",
        "数学（数学ⅢCまで）",
        "公民",
        "英語",
        "物理基礎",
        "物理",
        "化学基礎",
        "化学",
        "生物基礎",
        "生物",
        "地学基礎",
        "地学",
        "世界史",
        "日本史",
        "地理",
        "倫理",
        "政治経済"
    ]
}

days = [f"8月{i}日" for i in range(1, 5)]
periods = [2, 3, 4, 5, 6]

# 先生の可用性（適切に設定）
teacher_availability = {
    "田中先生": {
        "8月1日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月2日": {2: False, 3: True, 4: True, 5: True, 6: False},
        "8月3日": {2: False, 3: True, 4: True, 5: True, 6: False},
        "8月4日": {2: False, 3: False, 4: True, 5: True, 6: True},
    },
    "鈴木先生": {
        "8月1日": {2: True, 3: True, 4: False, 5: False, 6: True},
        "8月2日": {2: True, 3: True, 4: False, 5: False, 6: True},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月4日": {2: True, 3: True, 4: False, 5: False, 6: True},
    },
    "高橋先生": {
        "8月1日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: False, 5: False, 6: True},
        "8月4日": {2: True, 3: True, 4: True, 5: False, 6: False},
    },
    "佐藤先生": {
        "8月1日": {2: False, 3: False, 4: True, 5: True, 6: False},
        "8月2日": {2: False, 3: False, 4: True, 5: True, 6: False},
        "8月3日": {2: False, 3: False, 4: True, 5: True, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: False, 6: False},
    }
}

student_availability = {
    "池田大輔": {
        "8月1日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月2日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月3日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月4日": {2: False, 3: False, 4: True, 5: True, 6: True},
    },
    "宮本蓮": {
        "8月1日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: False, 6: False},
    },
    "三浦咲": {
        "8月1日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月3日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月4日": {2: False, 3: False, 4: False, 5: False, 6: False},
    },
    "西村健一": {
        "8月1日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月2日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月4日": {2: False, 3: False, 4: False, 5: False, 6: False},
    },
    "中野陽菜": {
        "8月1日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月2日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月4日": {2: False, 3: False, 4: False, 5: False, 6: False},
    },
    "大塚翔": {
        "8月1日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: False, 6: False},
    },
    "福田優": {
        "8月1日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月2日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月3日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月4日": {2: False, 3: False, 4: True, 5: True, 6: True},
    },
    "長谷川匠": {
        "8月1日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月3日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月4日": {2: False, 3: False, 4: False, 5: False, 6: False},
    }
}
can_teach = {
    "田中先生": {
        # elementary
        "elementary_国語": False, "elementary_算数": False, "elementary_理科": False, "elementary_社会": False, "elementary_英語": False,
        # middle
        "middle_国語": False, "middle_数学": True, "middle_理科": True, "middle_社会": False, "middle_英語": True,
        # high
        "high_国語": False, "high_数学（数学ⅡBまで）": False, "high_数学（数学ⅢCまで）": False, "high_公民": False, "high_英語": False, "high_物理基礎": False, "high_物理": False, "high_化学基礎": False, "high_化学": False, "high_生物基礎": False, "high_生物": False, "high_地学基礎": False, "high_地学": False, "high_世界史": False, "high_日本史": False, "high_地理": False, "high_倫理": False, "high_政治経済": False
    },
    "鈴木先生": {
        # elementary
        "elementary_国語": False, "elementary_算数": False, "elementary_理科": False, "elementary_社会": False, "elementary_英語": False,
        # middle
        "middle_国語": True, "middle_数学": True, "middle_理科": True, "middle_社会": True, "middle_英語": True,
        # high
        "high_国語": True, "high_数学（数学ⅡBまで）": False, "high_数学（数学ⅢCまで）": False, "high_公民": False, "high_英語": True, "high_物理基礎": False, "high_物理": False, "high_化学基礎": False, "high_化学": False, "high_生物基礎": False, "high_生物": True, "high_地学基礎": False, "high_地学": False, "high_世界史": False, "high_日本史": False, "high_地理": False, "high_倫理": False, "high_政治経済": False
    },
    "高橋先生": {
        # elementary
        "elementary_国語": False, "elementary_算数": False, "elementary_理科": False, "elementary_社会": False, "elementary_英語": False,
        # middle
        "middle_国語": False, "middle_数学": True, "middle_理科": True, "middle_社会": False, "middle_英語": False,
        # high
        "high_国語": False, "high_数学（数学ⅡBまで）": False, "high_数学（数学ⅢCまで）": False, "high_公民": False, "high_英語": False, "high_物理基礎": False, "high_物理": False, "high_化学基礎": False, "high_化学": False, "high_生物基礎": False, "high_生物": False, "high_地学基礎": False, "high_地学": False, "high_世界史": False, "high_日本史": False, "high_地理": False, "high_倫理": False, "high_政治経済": False
    },
    "佐藤先生": {
        # elementary
        "elementary_国語": False, "elementary_算数": False, "elementary_理科": False, "elementary_社会": False, "elementary_英語": False,
        # middle
        "middle_国語": True, "middle_数学": False, "middle_理科": False, "middle_社会": False, "middle_英語": True,
        # high
        "high_国語": False, "high_数学（数学ⅡBまで）": False, "high_数学（数学ⅢCまで）": False, "high_公民": False, "high_英語": False, "high_物理基礎": True, "high_物理": True, "high_化学基礎": False, "high_化学": False, "high_生物基礎": False, "high_生物": False, "high_地学基礎": False, "high_地学": False, "high_世界史": False, "high_日本史": False, "high_地理": True, "high_倫理": False, "high_政治経済": False
    }
}

# 各生徒のレギュラー授業（適切に設定）
regular_lessons = {
    "池田大輔": {
        "8月1日": [],
        "8月2日": [{"subject": "middle_英語", "period": 2, "teacher": "鈴木先生"}],
        "8月3日": [{"subject": "middle_国語", "period": 3, "teacher": "松本先生"}],
        "8月4日": [{"subject": "middle_数学", "period": 5, "teacher": "松本先生"}],
    },
    "宮本蓮": {
        "8月1日": [],
        "8月2日": [{"subject": "middle_国語", "period": 4, "teacher": "田中先生"}],
        "8月3日": [{"subject": "middle_英語", "period": 3, "teacher": "山本先生"}],
        "8月4日": [{"subject": "middle_数学", "period": 4, "teacher": "高橋先生"}],
    },
    "三浦咲": {
        "8月1日": [{"subject": "middle_数学", "period": 2, "teacher": "鈴木先生"}],
        "8月2日": [{"subject": "middle_英語", "period": 5, "teacher": "田中先生"}],
        "8月3日": [{"subject": "middle_国語", "period": 5, "teacher": "山本先生"}],
        "8月4日": [],
    },
    "西村健一": {
        "8月1日": [{"subject": "middle_国語", "period": 6, "teacher": "伊藤先生"}],
        "8月2日": [{"subject": "middle_数学", "period": 3, "teacher": "高橋先生"}],
        "8月3日": [{"subject": "middle_英語", "period": 2, "teacher": "田中先生"}],
        "8月4日": [],
    },
    "中野陽菜": {
        "8月1日": [{"subject": "middle_英語", "period": 5, "teacher": "鈴木先生"}],
        "8月2日": [{"subject": "middle_数学", "period": 5, "teacher": "鈴木先生"}],
        "8月3日": [{"subject": "middle_国語", "period": 4, "teacher": "渡辺先生"}],
        "8月4日": [],
    },
    "大塚翔": {
        "8月1日": [{"subject": "middle_国語", "period": 4, "teacher": "伊藤先生"}],
        "8月2日": [{"subject": "middle_英語", "period": 4, "teacher": "田中先生"}],
        "8月3日": [],
        "8月4日": [{"subject": "middle_数学", "period": 3, "teacher": "高橋先生"}],
    },
    "福田優": {
        "8月1日": [],
        "8月2日": [{"subject": "middle_国語", "period": 6, "teacher": "渡辺先生"}],
        "8月3日": [{"subject": "middle_英語", "period": 2, "teacher": "田中先生"}],
        "8月4日": [{"subject": "middle_数学", "period": 3, "teacher": "松本先生"}],
    },
    "長谷川匠": {
        "8月1日": [{"subject": "middle_数学", "period": 2, "teacher": "田中先生"}],
        "8月2日": [{"subject": "middle_英語", "period": 3, "teacher": "鈴木先生"}],
        "8月3日": [],
        "8月4日": [{"subject": "middle_国語", "period": 6, "teacher": "渡辺先生"}],
    }
}

# 各生徒が必要とするコマ数の設定をより現実的に
required_lessons = {
    "池田大輔": {
        "middle_国語": 1,
        "middle_数学": 1,
        "middle_理科": 1,
        "middle_社会": 1,
        "middle_英語": 1
    },
    "宮本蓮": {
        "middle_国語": 0,
        "middle_数学": 0,
        "middle_理科": 2,
        "middle_社会": 0,
        "middle_英語": 0
    },
    "三浦咲": {
        "middle_国語": 0,
        "middle_数学": 2,
        "middle_理科": 0,
        "middle_社会": 0,
        "middle_英語": 0
    },
    "西村健一": {
        "middle_国語": 0,
        "middle_数学": 2,
        "middle_理科": 0,
        "middle_社会": 1,
        "middle_英語": 1
    },
    "中野陽菜": {
        "middle_国語": 0,
        "middle_数学": 0,
        "middle_理科": 0,
        "middle_社会": 1,
        "middle_英語": 1
    },
    "大塚翔": {
        "middle_国語": 1,
        "middle_数学": 0,
        "middle_理科": 0,
        "middle_社会": 0,
        "middle_英語": 2
    },
    "福田優": {
        "middle_国語": 1,
        "middle_数学": 2,
        "middle_理科": 0,
        "middle_社会": 0,
        "middle_英語": 0
    },
    "長谷川匠": {
        "middle_国語": 0,
        "middle_数学": 0,
        "middle_理科": 1,
        "middle_社会": 2,
        "middle_英語": 1
    }
}


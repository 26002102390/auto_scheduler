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
        "8月1日": {2: False, 3: False, 4: True, 5: True, 6: False},
        "8月2日": {2: False, 3: False, 4: True, 5: True, 6: False},
        "8月3日": {2: False, 3: False, 4: True, 5: True, 6: False},
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
    },
    "伊藤先生": {
        "8月1日": {2: True, 3: True, 4: False, 5: False, 6: True},
        "8月2日": {2: True, 3: True, 4: False, 5: False, 6: True},
        "8月3日": {2: True, 3: True, 4: False, 5: False, 6: True},
        "8月4日": {2: True, 3: True, 4: False, 5: False, 6: True},
    },
    "渡辺先生": {
        "8月1日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: True, 6: False},
    },
    "山本先生": {
        "8月1日": {2: True, 3: True, 4: False, 5: False, 6: True},
        "8月2日": {2: True, 3: True, 4: False, 5: False, 6: True},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月4日": {2: False, 3: False, 4: True, 5: True, 6: False},
    },
    "中村先生": {
        "8月1日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月2日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月3日": {2: False, 3: False, 4: True, 5: True, 6: False},
        "8月4日": {2: False, 3: False, 4: True, 5: True, 6: False},
    },
    "小林先生": {
        "8月1日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月2日": {2: False, 3: False, 4: True, 5: True, 6: False},
        "8月3日": {2: False, 3: False, 4: True, 5: True, 6: False},
        "8月4日": {2: False, 3: False, 4: True, 5: True, 6: False},
    },
    "加藤先生": {
        "8月1日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月2日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月3日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月4日": {2: False, 3: False, 4: True, 5: True, 6: True},
    },
    "吉田先生": {
        "8月1日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月4日": {2: True, 3: True, 4: False, 5: False, 6: False},
    },
    "松本先生": {
        "8月1日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月4日": {2: True, 3: True, 4: False, 5: False, 6: False},
    }
}

# 生徒の可用性（適切に設定）
student_availability = {
    "山田太郎": {
        "8月1日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月3日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: True, 6: True},
    },
    "佐々木花子": {
        "8月1日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: False, 6: False},
    },
    "藤田翔": {
        "8月1日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月3日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: True, 6: True},
    },
    "近藤優": {
        "8月1日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月3日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: False, 6: False},
    },
    "木村直人": {
        "8月1日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月2日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月4日": {2: True, 3: True, 4: True, 5: True, 6: True},
    },
    "川上健": {
        "8月1日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月4日": {2: True, 3: True, 4: True, 5: True, 6: True},
    },
    "坂本亮": {
        "8月1日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月2日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月3日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月4日": {2: False, 3: False, 4: False, 5: False, 6: False},
    },
    "井上誠": {
        "8月1日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月2日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月3日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月4日": {2: False, 3: False, 4: True, 5: True, 6: True},
    },
    "原田愛": {
        "8月1日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: True, 6: False},
    },
    "森本翔子": {
        "8月1日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月2日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月4日": {2: True, 3: True, 4: True, 5: True, 6: True},
    },
    "石井拓也": {
        "8月1日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月2日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月4日": {2: False, 3: False, 4: False, 5: False, 6: False},
    },
    "武田恵": {
        "8月1日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月2日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月3日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月4日": {2: False, 3: False, 4: True, 5: True, 6: True},
    },
    "岡本真": {
        "8月1日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月2日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月3日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月4日": {2: False, 3: False, 4: True, 5: True, 6: True},
    },
    "小川舞": {
        "8月1日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月3日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: False, 6: False},
    },
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
    },
    "村上結": {
        "8月1日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月2日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月3日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: True, 6: True},
    },
    "白井航": {
        "8月1日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月2日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月3日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月4日": {2: False, 3: False, 4: True, 5: True, 6: True},
    },
    "橋本悠": {
        "8月1日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: True, 6: False},
    },
    "五十嵐和": {
        "8月1日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月2日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月4日": {2: False, 3: False, 4: False, 5: False, 6: False},
    },
    "柴田雅": {
        "8月1日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: False, 6: False},
    },
    "本田千夏": {
        "8月1日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: False, 6: False},
    },
    "和田亮太": {
        "8月1日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月2日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: True, 6: True},
    },
    "菊池誠": {
        "8月1日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月2日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月4日": {2: True, 3: True, 4: True, 5: True, 6: True},
    },
    "野口未来": {
        "8月1日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月4日": {2: True, 3: True, 4: False, 5: False, 6: False},
    },
    "高木健": {
        "8月1日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月2日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月4日": {2: True, 3: True, 4: True, 5: True, 6: True},
    },
    "浜田裕": {
        "8月1日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月2日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月4日": {2: True, 3: True, 4: False, 5: False, 6: False},
    },
    "岡崎萌": {
        "8月1日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: False, 6: False},
    },
    "松井翼": {
        "8月1日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月2日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月3日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月4日": {2: False, 3: False, 4: True, 5: True, 6: True},
    },
    "東出拓真": {
        "8月1日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月2日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月3日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月4日": {2: True, 3: True, 4: True, 5: False, 6: False},
    },
    "栗原志穂": {
        "8月1日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: False, 6: False},
    },
    "矢野大輔": {
        "8月1日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月4日": {2: False, 3: False, 4: False, 5: False, 6: False},
    },
    "安田直美": {
        "8月1日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: True, 6: False},
    },
    "新垣翔": {
        "8月1日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月3日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月4日": {2: True, 3: True, 4: False, 5: False, 6: False},
    },
    "大西健一": {
        "8月1日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月2日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月3日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月4日": {2: False, 3: False, 4: False, 5: False, 6: False},
    },
    "篠田莉奈": {
        "8月1日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月2日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月4日": {2: True, 3: True, 4: True, 5: True, 6: True},
    },
    "広瀬駿": {
        "8月1日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: True},
        "8月4日": {2: True, 3: True, 4: True, 5: True, 6: False},
    },
    "萩原悠": {
        "8月1日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: False, 5: False, 6: False},
        "8月4日": {2: False, 3: False, 4: False, 5: False, 6: False},
    },
    "桜井智": {
        "8月1日": {2: False, 3: False, 4: False, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: True, 6: True},
    },
    "藤本綾": {
        "8月1日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: True, 6: False},
        "8月4日": {2: True, 3: True, 4: True, 5: True, 6: False},
    },
    "川端翼": {
        "8月1日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月2日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月3日": {2: False, 3: False, 4: True, 5: True, 6: True},
        "8月4日": {2: False, 3: False, 4: True, 5: True, 6: True},
    },
    "井村悠斗": {
        "8月1日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月2日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月3日": {2: True, 3: True, 4: True, 5: False, 6: False},
        "8月4日": {2: False, 3: False, 4: False, 5: False, 6: False},
    }
}

can_teach = {
    "田中先生": {
        # elementary
        "elementary_国語": False, "elementary_算数": False, "elementary_理科": False, "elementary_社会": False, "elementary_英語": False,
        # middle
        "middle_国語": False, "middle_数学": True, "middle_理科": False, "middle_社会": False, "middle_英語": True,
        # high
        "high_国語": False, "high_数学（数学ⅡBまで）": False, "high_数学（数学ⅢCまで）": False, "high_公民": False, "high_英語": False, "high_物理基礎": False, "high_物理": False, "high_化学基礎": False, "high_化学": False, "high_生物基礎": False, "high_生物": False, "high_地学基礎": False, "high_地学": False, "high_世界史": False, "high_日本史": False, "high_地理": False, "high_倫理": False, "high_政治経済": False
    },
    "鈴木先生": {
        # elementary
        "elementary_国語": False, "elementary_算数": False, "elementary_理科": False, "elementary_社会": False, "elementary_英語": False,
        # middle
        "middle_国語": False, "middle_数学": True, "middle_理科": False, "middle_社会": True, "middle_英語": True,
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
        "middle_国語": False, "middle_数学": False, "middle_理科": False, "middle_社会": False, "middle_英語": False,
        # high
        "high_国語": False, "high_数学（数学ⅡBまで）": False, "high_数学（数学ⅢCまで）": False, "high_公民": False, "high_英語": False, "high_物理基礎": True, "high_物理": True, "high_化学基礎": False, "high_化学": False, "high_生物基礎": False, "high_生物": False, "high_地学基礎": False, "high_地学": False, "high_世界史": False, "high_日本史": False, "high_地理": True, "high_倫理": False, "high_政治経済": False
    },
    "伊藤先生": {
        # elementary
        "elementary_国語": False, "elementary_算数": False, "elementary_理科": False, "elementary_社会": True, "elementary_英語": True,
        # middle
        "middle_国語": False, "middle_数学": False, "middle_理科": False, "middle_社会": False, "middle_英語": False,
        # high
        "high_国語": False, "high_数学（数学ⅡBまで）": False, "high_数学（数学ⅢCまで）": False, "high_公民": True, "high_英語": False, "high_物理基礎": True, "high_物理": False, "high_化学基礎": False, "high_化学": False, "high_生物基礎": False, "high_生物": False, "high_地学基礎": False, "high_地学": False, "high_世界史": False, "high_日本史": False, "high_地理": False, "high_倫理": False, "high_政治経済": False
    },
    "渡辺先生": {
        # elementary
        "elementary_国語": True, "elementary_算数": False, "elementary_理科": False, "elementary_社会": True, "elementary_英語": True,
        # middle
        "middle_国語": False, "middle_数学": False, "middle_理科": False, "middle_社会": False, "middle_英語": False,
        # high
        "high_国語": False, "high_数学（数学ⅡBまで）": True, "high_数学（数学ⅢCまで）": False, "high_公民": False, "high_英語": False, "high_物理基礎": False, "high_物理": False, "high_化学基礎": True, "high_化学": False, "high_生物基礎": True, "high_生物": False, "high_地学基礎": False, "high_地学": False, "high_世界史": False, "high_日本史": False, "high_地理": False, "high_倫理": False, "high_政治経済": False
    },
    "山本先生": {
        # elementary
        "elementary_国語": False, "elementary_算数": False, "elementary_理科": False, "elementary_社会": False, "elementary_英語": False,
        # middle
        "middle_国語": False, "middle_数学": False, "middle_理科": True, "middle_社会": False, "middle_英語": True,
        # high
        "high_国語": False, "high_数学（数学ⅡBまで）": False, "high_数学（数学ⅢCまで）": False, "high_公民": False, "high_英語": False, "high_物理基礎": False, "high_物理": False, "high_化学基礎": False, "high_化学": False, "high_生物基礎": False, "high_生物": False, "high_地学基礎": False, "high_地学": False, "high_世界史": False, "high_日本史": False, "high_地理": False, "high_倫理": False, "high_政治経済": False
    },
    "中村先生": {
        # elementary
        "elementary_国語": False, "elementary_算数": False, "elementary_理科": True, "elementary_社会": True, "elementary_英語": True,
        # middle
        "middle_国語": False, "middle_数学": False, "middle_理科": False, "middle_社会": False, "middle_英語": False,
        # high
        "high_国語": False, "high_数学（数学ⅡBまで）": True, "high_数学（数学ⅢCまで）": True, "high_公民": False, "high_英語": False, "high_物理基礎": False, "high_物理": False, "high_化学基礎": False, "high_化学": False, "high_生物基礎": False, "high_生物": False, "high_地学基礎": False, "high_地学": False, "high_世界史": True, "high_日本史": False, "high_地理": False, "high_倫理": False, "high_政治経済": False
    },
    "小林先生": {
        # elementary
        "elementary_国語": False, "elementary_算数": True, "elementary_理科": False, "elementary_社会": False, "elementary_英語": True,
        # middle
        "middle_国語": False, "middle_数学": False, "middle_理科": False, "middle_社会": False, "middle_英語": False,
        # high
        "high_国語": False, "high_数学（数学ⅡBまで）": False, "high_数学（数学ⅢCまで）": False, "high_公民": False, "high_英語": False, "high_物理基礎": False, "high_物理": False, "high_化学基礎": True, "high_化学": False, "high_生物基礎": False, "high_生物": False, "high_地学基礎": False, "high_地学": True, "high_世界史": False, "high_日本史": True, "high_地理": False, "high_倫理": False, "high_政治経済": False
    },
    "加藤先生": {
        # elementary
        "elementary_国語": False, "elementary_算数": False, "elementary_理科": False, "elementary_社会": False, "elementary_英語": False,
        # middle
        "middle_国語": False, "middle_数学": False, "middle_理科": True, "middle_社会": True, "middle_英語": False,
        # high
        "high_国語": False, "high_数学（数学ⅡBまで）": False, "high_数学（数学ⅢCまで）": False, "high_公民": False, "high_英語": False, "high_物理基礎": False, "high_物理": False, "high_化学基礎": False, "high_化学": False, "high_生物基礎": False, "high_生物": False, "high_地学基礎": False, "high_地学": False, "high_世界史": False, "high_日本史": True, "high_地理": False, "high_倫理": False, "high_政治経済": True
    },
    "吉田先生": {
        # elementary
        "elementary_国語": True, "elementary_算数": False, "elementary_理科": True, "elementary_社会": False, "elementary_英語": True,
        # middle
        "middle_国語": False, "middle_数学": False, "middle_理科": False, "middle_社会": False, "middle_英語": False,
        # high
        "high_国語": False, "high_数学（数学ⅡBまで）": False, "high_数学（数学ⅢCまで）": False, "high_公民": False, "high_英語": False, "high_物理基礎": False, "high_物理": False, "high_化学基礎": False, "high_化学": True, "high_生物基礎": False, "high_生物": False, "high_地学基礎": True, "high_地学": False, "high_世界史": False, "high_日本史": False, "high_地理": False, "high_倫理": True, "high_政治経済": False
    },
    "松本先生": {
        # elementary
        "elementary_国語": False, "elementary_算数": True, "elementary_理科": False, "elementary_社会": True, "elementary_英語": False,
        # middle
        "middle_国語": True, "middle_数学": True, "middle_理科": False, "middle_社会": True, "middle_英語": False,
        # high
        "high_国語": False, "high_数学（数学ⅡBまで）": False, "high_数学（数学ⅢCまで）": False, "high_公民": False, "high_英語": False, "high_物理基礎": False, "high_物理": False, "high_化学基礎": False, "high_化学": True, "high_生物基礎": False, "high_生物": False, "high_地学基礎": False, "high_地学": False, "high_世界史": False, "high_日本史": False, "high_地理": False, "high_倫理": False, "high_政治経済": False
    }
}

# 各生徒のレギュラー授業（適切に設定）
regular_lessons = {
    "山田太郎": {
        "8月1日": [{"subject": "elementary_英語", "period": 5, "teacher": "小林先生"}],
        "8月2日": [{"subject": "elementary_国語", "period": 6, "teacher": "渡辺先生"}],
        "8月3日": [],
        "8月4日": [{"subject": "elementary_算数", "period": 3, "teacher": "松本先生"}],
    },
    "佐々木花子": {
        "8月1日": [{"subject": "elementary_国語", "period": 4, "teacher": "吉田先生"}],
        "8月2日": [{"subject": "elementary_算数", "period": 2, "teacher": "松本先生"}],
        "8月3日": [],
        "8月4日": [{"subject": "elementary_英語", "period": 4, "teacher": "吉田先生"}],
    },
    "藤田翔": {
        "8月1日": [{"subject": "elementary_英語", "period": 3, "teacher": "吉田先生"}],
        "8月2日": [{"subject": "elementary_算数", "period": 4, "teacher": "松本先生"}],
        "8月3日": [{"subject": "elementary_国語", "period": 3, "teacher": "渡辺先生"}],
        "8月4日": [],
    },
    "近藤優": {
        "8月1日": [{"subject": "elementary_英語", "period": 5, "teacher": "吉田先生"}],
        "8月2日": [{"subject": "elementary_算数", "period": 3, "teacher": "小林先生"}],
        "8月3日": [],
        "8月4日": [{"subject": "elementary_国語", "period": 4, "teacher": "渡辺先生"}],
    },
    "木村直人": {
        "8月1日": [{"subject": "elementary_算数", "period": 2, "teacher": "松本先生"}],
        "8月2日": [{"subject": "elementary_英語", "period": 3, "teacher": "小林先生"}],
        "8月3日": [],
        "8月4日": [{"subject": "elementary_国語", "period": 5, "teacher": "吉田先生"}],
    },
    "川上健": {
        "8月1日": [{"subject": "elementary_算数", "period": 3, "teacher": "松本先生"}],
        "8月2日": [],
        "8月3日": [{"subject": "elementary_英語", "period": 6, "teacher": "小林先生"}],
        "8月4日": [{"subject": "elementary_国語", "period": 6, "teacher": "吉田先生"}],
    },
    "坂本亮": {
        "8月1日": [],
        "8月2日": [{"subject": "middle_英語", "period": 3, "teacher": "田中先生"}],
        "8月3日": [{"subject": "middle_国語", "period": 3, "teacher": "高橋先生"}],
        "8月4日": [{"subject": "middle_数学", "period": 4, "teacher": "鈴木先生"}],
    },
    "井上誠": {
        "8月1日": [{"subject": "middle_国語", "period": 4, "teacher": "佐藤先生"}],
        "8月2日": [{"subject": "middle_英語", "period": 5, "teacher": "鈴木先生"}],
        "8月3日": [{"subject": "middle_数学", "period": 2, "teacher": "高橋先生"}],
        "8月4日": [],
    },
    "原田愛": {
        "8月1日": [{"subject": "middle_数学", "period": 5, "teacher": "鈴木先生"}],
        "8月2日": [{"subject": "middle_国語", "period": 5, "teacher": "松本先生"}],
        "8月3日": [],
        "8月4日": [{"subject": "middle_英語", "period": 6, "teacher": "鈴木先生"}],
    },
    "森本翔子": {
        "8月1日": [{"subject": "middle_数学", "period": 6, "teacher": "田中先生"}],
        "8月2日": [{"subject": "middle_国語", "period": 6, "teacher": "吉田先生"}],
        "8月3日": [{"subject": "middle_英語", "period": 4, "teacher": "田中先生"}],
        "8月4日": [],
    },
    "石井拓也": {
        "8月1日": [],
        "8月2日": [{"subject": "middle_英語", "period": 4, "teacher": "山本先生"}],
        "8月3日": [{"subject": "middle_国語", "period": 2, "teacher": "佐藤先生"}],
        "8月4日": [{"subject": "middle_数学", "period": 5, "teacher": "鈴木先生"}],
    },
    "武田恵": {
        "8月1日": [{"subject": "middle_数学", "period": 6, "teacher": "松本先生"}],
        "8月2日": [{"subject": "middle_国語", "period": 2, "teacher": "中村先生"}],
        "8月3日": [],
        "8月4日": [{"subject": "middle_英語", "period": 4, "teacher": "鈴木先生"}],
    },
    "岡本真": {
        "8月1日": [{"subject": "middle_数学", "period": 2, "teacher": "松本先生"}],
        "8月2日": [{"subject": "middle_英語", "period": 5, "teacher": "鈴木先生"}],
        "8月3日": [{"subject": "middle_国語", "period": 3, "teacher": "吉田先生"}],
        "8月4日": [],
    },
    "小川舞": {
        "8月1日": [{"subject": "middle_英語", "period": 5, "teacher": "田中先生"}],
        "8月2日": [],
        "8月3日": [{"subject": "middle_国語", "period": 5, "teacher": "渡辺先生"}],
        "8月4日": [{"subject": "middle_数学", "period": 3, "teacher": "高橋先生"}],
    },
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
    },
    "村上結": {
        "8月1日": [{"subject": "middle_英語", "period": 4, "teacher": "山本先生"}],
        "8月2日": [{"subject": "middle_数学", "period": 6, "teacher": "高橋先生"}],
        "8月3日": [{"subject": "middle_国語", "period": 2, "teacher": "高橋先生"}],
        "8月4日": [],
    },
    "白井航": {
        "8月1日": [],
        "8月2日": [{"subject": "middle_数学", "period": 2, "teacher": "田中先生"}],
        "8月3日": [{"subject": "middle_英語", "period": 2, "teacher": "田中先生"}],
        "8月4日": [{"subject": "middle_国語", "period": 4, "teacher": "中村先生"}],
    },
    "橋本悠": {
        "8月1日": [{"subject": "middle_英語", "period": 3, "teacher": "田中先生"}],
        "8月2日": [{"subject": "middle_国語", "period": 5, "teacher": "伊藤先生"}],
        "8月3日": [{"subject": "middle_数学", "period": 6, "teacher": "松本先生"}],
        "8月4日": [],
    },
    "五十嵐和": {
        "8月1日": [{"subject": "middle_数学", "period": 4, "teacher": "松本先生"}],
        "8月2日": [{"subject": "middle_国語", "period": 6, "teacher": "山本先生"}],
        "8月3日": [{"subject": "middle_英語", "period": 2, "teacher": "田中先生"}],
        "8月4日": [],
    },
    "柴田雅": {
        "8月1日": [],
        "8月2日": [{"subject": "middle_英語", "period": 3, "teacher": "田中先生"}],
        "8月3日": [{"subject": "middle_国語", "period": 5, "teacher": "小林先生"}],
        "8月4日": [{"subject": "middle_数学", "period": 5, "teacher": "田中先生"}],
    },
    "本田千夏": {
        "8月1日": [],
        "8月2日": [{"subject": "middle_英語", "period": 6, "teacher": "山本先生"}],
        "8月3日": [{"subject": "middle_国語", "period": 2, "teacher": "山本先生"}],
        "8月4日": [{"subject": "middle_数学", "period": 6, "teacher": "鈴木先生"}],
    },
    "和田亮太": {
        "8月1日": [{"subject": "middle_国語", "period": 5, "teacher": "山本先生"}],
        "8月2日": [],
        "8月3日": [{"subject": "middle_数学", "period": 5, "teacher": "田中先生"}],
        "8月4日": [{"subject": "middle_英語", "period": 2, "teacher": "山本先生"}],
    },
    "菊池誠": {
        "8月1日": [{"subject": "middle_国語", "period": 3, "teacher": "加藤先生"}],
        "8月2日": [{"subject": "middle_数学", "period": 6, "teacher": "高橋先生"}],
        "8月3日": [{"subject": "middle_英語", "period": 3, "teacher": "山本先生"}],
        "8月4日": [],
    },
    "野口未来": {
        "8月1日": [{"subject": "high_国語", "period": 2, "teacher": "鈴木先生"}],
        "8月2日": [{"subject": "high_数学", "period": 6, "teacher": "佐藤先生"}],
        "8月3日": [],
        "8月4日": [{"subject": "high_英語", "period": 5, "teacher": "鈴木先生"}],
    },
    "高木健": {
        "8月1日": [{"subject": "high_国語", "period": 3, "teacher": "鈴木先生"}],
        "8月2日": [{"subject": "high_数学", "period": 6, "teacher": "中村先生"}],
        "8月3日": [{"subject": "high_英語", "period": 3, "teacher": "鈴木先生"}],
        "8月4日": [],
    },
    "浜田裕": {
        "8月1日": [{"subject": "high_英語", "period": 6, "teacher": "鈴木先生"}],
        "8月2日": [{"subject": "high_国語", "period": 3, "teacher": "鈴木先生"}],
        "8月3日": [{"subject": "high_数学", "period": 4, "teacher": "中村先生"}],
        "8月4日": [],
    },
    "岡崎萌": {
        "8月1日": [{"subject": "high_国語", "period": 6, "teacher": "鈴木先生"}],
        "8月2日": [{"subject": "high_英語", "period": 3, "teacher": "鈴木先生"}],
        "8月3日": [],
        "8月4日": [{"subject": "high_数学", "period": 5, "teacher": "伊藤先生"}],
    },
    "松井翼": {
        "8月1日": [{"subject": "high_英語", "period": 4, "teacher": "鈴木先生"}],
        "8月2日": [{"subject": "high_数学", "period": 6, "teacher": "田中先生"}],
        "8月3日": [{"subject": "high_国語", "period": 2, "teacher": "鈴木先生"}],
        "8月4日": [],
    },
    "東出拓真": {
        "8月1日": [{"subject": "high_数学", "period": 3, "teacher": "中村先生"}],
        "8月2日": [{"subject": "high_英語", "period": 4, "teacher": "鈴木先生"}],
        "8月3日": [{"subject": "high_国語", "period": 4, "teacher": "鈴木先生"}],
        "8月4日": [],
    },
    "栗原志穂": {
        "8月1日": [{"subject": "high_英語", "period": 6, "teacher": "鈴木先生"}],
        "8月2日": [],
        "8月3日": [{"subject": "high_国語", "period": 3, "teacher": "鈴木先生"}],
        "8月4日": [{"subject": "high_数学", "period": 5, "teacher": "松本先生"}],
    },
    "矢野大輔": {
        "8月1日": [],
        "8月2日": [{"subject": "high_国語", "period": 3, "teacher": "鈴木先生"}],
        "8月3日": [{"subject": "high_英語", "period": 3, "teacher": "鈴木先生"}],
        "8月4日": [{"subject": "high_数学", "period": 4, "teacher": "渡辺先生"}],
    },
    "安田直美": {
        "8月1日": [{"subject": "high_数学", "period": 4, "teacher": "田中先生"}],
        "8月2日": [{"subject": "high_英語", "period": 6, "teacher": "鈴木先生"}],
        "8月3日": [],
        "8月4日": [{"subject": "high_国語", "period": 4, "teacher": "鈴木先生"}],
    },
    "新垣翔": {
        "8月1日": [{"subject": "high_数学", "period": 6, "teacher": "渡辺先生"}],
        "8月2日": [],
        "8月3日": [{"subject": "high_国語", "period": 2, "teacher": "鈴木先生"}],
        "8月4日": [{"subject": "high_英語", "period": 2, "teacher": "鈴木先生"}],
    },
    "大西健一": {
        "8月1日": [{"subject": "high_英語", "period": 5, "teacher": "鈴木先生"}],
        "8月2日": [],
        "8月3日": [{"subject": "high_国語", "period": 2, "teacher": "鈴木先生"}],
        "8月4日": [{"subject": "high_数学", "period": 3, "teacher": "中村先生"}],
    },
    "篠田莉奈": {
        "8月1日": [],
        "8月2日": [{"subject": "high_数学", "period": 6, "teacher": "田中先生"}],
        "8月3日": [{"subject": "high_英語", "period": 6, "teacher": "鈴木先生"}],
        "8月4日": [{"subject": "high_国語", "period": 3, "teacher": "鈴木先生"}],
    },
    "広瀬駿": {
        "8月1日": [{"subject": "high_国語", "period": 4, "teacher": "鈴木先生"}],
        "8月2日": [],
        "8月3日": [{"subject": "high_英語", "period": 3, "teacher": "鈴木先生"}],
        "8月4日": [{"subject": "high_数学", "period": 6, "teacher": "田中先生"}],
    },
    "萩原悠": {
        "8月1日": [],
        "8月2日": [{"subject": "high_数学", "period": 2, "teacher": "佐藤先生"}],
        "8月3日": [{"subject": "high_英語", "period": 3, "teacher": "鈴木先生"}],
        "8月4日": [{"subject": "high_国語", "period": 3, "teacher": "鈴木先生"}],
    },
    "桜井智": {
        "8月1日": [{"subject": "high_英語", "period": 2, "teacher": "鈴木先生"}],
        "8月2日": [{"subject": "high_国語", "period": 6, "teacher": "鈴木先生"}],
        "8月3日": [{"subject": "high_数学", "period": 4, "teacher": "中村先生"}],
        "8月4日": [],
    },
    "藤本綾": {
        "8月1日": [{"subject": "high_数学", "period": 2, "teacher": "吉田先生"}],
        "8月2日": [{"subject": "high_国語", "period": 6, "teacher": "鈴木先生"}],
        "8月3日": [{"subject": "high_英語", "period": 6, "teacher": "鈴木先生"}],
        "8月4日": [],
    },
    "川端翼": {
        "8月1日": [],
        "8月2日": [{"subject": "high_英語", "period": 3, "teacher": "鈴木先生"}],
        "8月3日": [{"subject": "high_数学", "period": 2, "teacher": "吉田先生"}],
        "8月4日": [{"subject": "high_国語", "period": 2, "teacher": "鈴木先生"}],
    },
    "井村悠斗": {
        "8月1日": [{"subject": "high_数学", "period": 5, "teacher": "鈴木先生"}],
        "8月2日": [{"subject": "high_国語", "period": 2, "teacher": "鈴木先生"}],
        "8月3日": [],
        "8月4日": [{"subject": "high_英語", "period": 3, "teacher": "鈴木先生"}],
    }
}

# 各生徒が必要とするコマ数の設定をより現実的に
required_lessons = {
    "山田太郎": {
        "elementary_国語": 2,
        "elementary_算数": 0,
        "elementary_理科": 2,
        "elementary_社会": 0,
        "elementary_英語": 0
    },
    "佐々木花子": {
        "elementary_国語": 0,
        "elementary_算数": 1,
        "elementary_理科": 0,
        "elementary_社会": 0,
        "elementary_英語": 0
    },
    "藤田翔": {
        "elementary_国語": 0,
        "elementary_算数": 1,
        "elementary_理科": 0,
        "elementary_社会": 0,
        "elementary_英語": 0
    },
    "近藤優": {
        "elementary_国語": 0,
        "elementary_算数": 0,
        "elementary_理科": 0,
        "elementary_社会": 0,
        "elementary_英語": 2
    },
    "木村直人": {
        "elementary_国語": 1,
        "elementary_算数": 0,
        "elementary_理科": 0,
        "elementary_社会": 0,
        "elementary_英語": 0
    },
    "川上健": {
        "elementary_国語": 0,
        "elementary_算数": 1,
        "elementary_理科": 0,
        "elementary_社会": 1,
        "elementary_英語": 0
    },
    "坂本亮": {
        "middle_国語": 0,
        "middle_数学": 0,
        "middle_理科": 0,
        "middle_社会": 1,
        "middle_英語": 0
    },
    "井上誠": {
        "middle_国語": 1,
        "middle_数学": 0,
        "middle_理科": 2,
        "middle_社会": 0,
        "middle_英語": 0
    },
    "原田愛": {
        "middle_国語": 0,
        "middle_数学": 0,
        "middle_理科": 0,
        "middle_社会": 0,
        "middle_英語": 0
    },
    "森本翔子": {
        "middle_国語": 0,
        "middle_数学": 0,
        "middle_理科": 0,
        "middle_社会": 0,
        "middle_英語": 0
    },
    "石井拓也": {
        "middle_国語": 0,
        "middle_数学": 0,
        "middle_理科": 0,
        "middle_社会": 0,
        "middle_英語": 0
    },
    "武田恵": {
        "middle_国語": 0,
        "middle_数学": 2,
        "middle_理科": 0,
        "middle_社会": 2,
        "middle_英語": 2
    },
    "岡本真": {
        "middle_国語": 0,
        "middle_数学": 1,
        "middle_理科": 1,
        "middle_社会": 0,
        "middle_英語": 0
    },
    "小川舞": {
        "middle_国語": 1,
        "middle_数学": 0,
        "middle_理科": 0,
        "middle_社会": 2,
        "middle_英語": 0
    },
    "池田大輔": {
        "middle_国語": 1,
        "middle_数学": 1,
        "middle_理科": 0,
        "middle_社会": 0,
        "middle_英語": 0
    },
    "宮本蓮": {
        "middle_国語": 0,
        "middle_数学": 0,
        "middle_理科": 0,
        "middle_社会": 0,
        "middle_英語": 0
    },
    "三浦咲": {
        "middle_国語": 0,
        "middle_数学": 0,
        "middle_理科": 0,
        "middle_社会": 0,
        "middle_英語": 0
    },
    "西村健一": {
        "middle_国語": 0,
        "middle_数学": 0,
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
        "middle_英語": 0
    },
    "福田優": {
        "middle_国語": 1,
        "middle_数学": 0,
        "middle_理科": 0,
        "middle_社会": 0,
        "middle_英語": 0
    },
    "長谷川匠": {
        "middle_国語": 0,
        "middle_数学": 0,
        "middle_理科": 1,
        "middle_社会": 0,
        "middle_英語": 1
    },
    "村上結": {
        "middle_国語": 0,
        "middle_数学": 0,
        "middle_理科": 0,
        "middle_社会": 1,
        "middle_英語": 0
    },
    "白井航": {
        "middle_国語": 2,
        "middle_数学": 0,
        "middle_理科": 0,
        "middle_社会": 1,
        "middle_英語": 0
    },
    "橋本悠": {
        "middle_国語": 0,
        "middle_数学": 0,
        "middle_理科": 0,
        "middle_社会": 0,
        "middle_英語": 0
    },
    "五十嵐和": {
        "middle_国語": 1,
        "middle_数学": 0,
        "middle_理科": 1,
        "middle_社会": 0,
        "middle_英語": 0
    },
    "柴田雅": {
        "middle_国語": 0,
        "middle_数学": 0,
        "middle_理科": 0,
        "middle_社会": 0,
        "middle_英語": 0
    },
    "本田千夏": {
        "middle_国語": 0,
        "middle_数学": 1,
        "middle_理科": 0,
        "middle_社会": 0,
        "middle_英語": 0
    },
    "和田亮太": {
        "middle_国語": 0,
        "middle_数学": 0,
        "middle_理科": 1,
        "middle_社会": 1,
        "middle_英語": 2
    },
    "菊池誠": {
        "middle_国語": 0,
        "middle_数学": 0,
        "middle_理科": 1,
        "middle_社会": 0,
        "middle_英語": 0
    },
    "野口未来": {
        "high_国語": 0,
        "high_数学（数学ⅡBまで）": 0,
        "high_数学（数学ⅢCまで）": 0,
        "high_公民": 0,
        "high_英語": 0,
        "high_物理基礎": 0,
        "high_物理": 0,
        "high_化学基礎": 0,
        "high_化学": 0,
        "high_生物基礎": 0,
        "high_生物": 0,
        "high_地学基礎": 0,
        "high_地学": 0,
        "high_世界史": 0,
        "high_日本史": 0,
        "high_地理": 0,
        "high_倫理": 0,
        "high_政治経済": 0
    },
    "高木健": {
        "high_国語": 0,
        "high_数学（数学ⅡBまで）": 0,
        "high_数学（数学ⅢCまで）": 0,
        "high_公民": 0,
        "high_英語": 0,
        "high_物理基礎": 0,
        "high_物理": 0,
        "high_化学基礎": 0,
        "high_化学": 0,
        "high_生物基礎": 0,
        "high_生物": 0,
        "high_地学基礎": 0,
        "high_地学": 0,
        "high_世界史": 0,
        "high_日本史": 0,
        "high_地理": 0,
        "high_倫理": 0,
        "high_政治経済": 0
    },
    "浜田裕": {
        "high_国語": 0,
        "high_数学（数学ⅡBまで）": 0,
        "high_数学（数学ⅢCまで）": 0,
        "high_公民": 0,
        "high_英語": 0,
        "high_物理基礎": 0,
        "high_物理": 0,
        "high_化学基礎": 0,
        "high_化学": 0,
        "high_生物基礎": 0,
        "high_生物": 0,
        "high_地学基礎": 0,
        "high_地学": 0,
        "high_世界史": 0,
        "high_日本史": 0,
        "high_地理": 0,
        "high_倫理": 0,
        "high_政治経済": 0
    },
    "岡崎萌": {
        "high_国語": 0,
        "high_数学（数学ⅡBまで）": 0,
        "high_数学（数学ⅢCまで）": 0,
        "high_公民": 0,
        "high_英語": 0,
        "high_物理基礎": 0,
        "high_物理": 0,
        "high_化学基礎": 0,
        "high_化学": 0,
        "high_生物基礎": 0,
        "high_生物": 0,
        "high_地学基礎": 0,
        "high_地学": 0,
        "high_世界史": 0,
        "high_日本史": 0,
        "high_地理": 0,
        "high_倫理": 0,
        "high_政治経済": 0
    },
    "松井翼": {
        "high_国語": 0,
        "high_数学（数学ⅡBまで）": 0,
        "high_数学（数学ⅢCまで）": 0,
        "high_公民": 0,
        "high_英語": 0,
        "high_物理基礎": 0,
        "high_物理": 0,
        "high_化学基礎": 0,
        "high_化学": 0,
        "high_生物基礎": 0,
        "high_生物": 0,
        "high_地学基礎": 0,
        "high_地学": 0,
        "high_世界史": 0,
        "high_日本史": 0,
        "high_地理": 0,
        "high_倫理": 0,
        "high_政治経済": 0
    },
    "東出拓真": {
        "high_国語": 0,
        "high_数学（数学ⅡBまで）": 0,
        "high_数学（数学ⅢCまで）": 0,
        "high_公民": 0,
        "high_英語": 0,
        "high_物理基礎": 0,
        "high_物理": 0,
        "high_化学基礎": 0,
        "high_化学": 0,
        "high_生物基礎": 0,
        "high_生物": 0,
        "high_地学基礎": 0,
        "high_地学": 0,
        "high_世界史": 0,
        "high_日本史": 0,
        "high_地理": 0,
        "high_倫理": 0,
        "high_政治経済": 0
    },
    "栗原志穂": {
        "high_国語": 0,
        "high_数学（数学ⅡBまで）": 0,
        "high_数学（数学ⅢCまで）": 0,
        "high_公民": 0,
        "high_英語": 0,
        "high_物理基礎": 0,
        "high_物理": 0,
        "high_化学基礎": 0,
        "high_化学": 0,
        "high_生物基礎": 0,
        "high_生物": 0,
        "high_地学基礎": 0,
        "high_地学": 0,
        "high_世界史": 0,
        "high_日本史": 0,
        "high_地理": 0,
        "high_倫理": 0,
        "high_政治経済": 0
    },
    "矢野大輔": {
        "high_国語": 0,
        "high_数学（数学ⅡBまで）": 0,
        "high_数学（数学ⅢCまで）": 0,
        "high_公民": 0,
        "high_英語": 0,
        "high_物理基礎": 0,
        "high_物理": 0,
        "high_化学基礎": 0,
        "high_化学": 0,
        "high_生物基礎": 0,
        "high_生物": 0,
        "high_地学基礎": 0,
        "high_地学": 0,
        "high_世界史": 0,
        "high_日本史": 0,
        "high_地理": 0,
        "high_倫理": 0,
        "high_政治経済": 0
    },
    "安田直美": {
        "high_国語": 0,
        "high_数学（数学ⅡBまで）": 0,
        "high_数学（数学ⅢCまで）": 0,
        "high_公民": 0,
        "high_英語": 0,
        "high_物理基礎": 0,
        "high_物理": 0,
        "high_化学基礎": 0,
        "high_化学": 0,
        "high_生物基礎": 0,
        "high_生物": 0,
        "high_地学基礎": 0,
        "high_地学": 0,
        "high_世界史": 0,
        "high_日本史": 0,
        "high_地理": 0,
        "high_倫理": 0,
        "high_政治経済": 0
    },
    "新垣翔": {
        "high_国語": 0,
        "high_数学（数学ⅡBまで）": 0,
        "high_数学（数学ⅢCまで）": 0,
        "high_公民": 0,
        "high_英語": 0,
        "high_物理基礎": 0,
        "high_物理": 0,
        "high_化学基礎": 0,
        "high_化学": 0,
        "high_生物基礎": 0,
        "high_生物": 0,
        "high_地学基礎": 0,
        "high_地学": 0,
        "high_世界史": 0,
        "high_日本史": 0,
        "high_地理": 0,
        "high_倫理": 0,
        "high_政治経済": 0
    },
    "大西健一": {
        "high_国語": 0,
        "high_数学（数学ⅡBまで）": 0,
        "high_数学（数学ⅢCまで）": 0,
        "high_公民": 0,
        "high_英語": 0,
        "high_物理基礎": 0,
        "high_物理": 0,
        "high_化学基礎": 0,
        "high_化学": 0,
        "high_生物基礎": 0,
        "high_生物": 0,
        "high_地学基礎": 0,
        "high_地学": 0,
        "high_世界史": 0,
        "high_日本史": 0,
        "high_地理": 0,
        "high_倫理": 0,
        "high_政治経済": 0
    },
    "篠田莉奈": {
        "high_国語": 0,
        "high_数学（数学ⅡBまで）": 0,
        "high_数学（数学ⅢCまで）": 0,
        "high_公民": 0,
        "high_英語": 0,
        "high_物理基礎": 0,
        "high_物理": 0,
        "high_化学基礎": 0,
        "high_化学": 0,
        "high_生物基礎": 0,
        "high_生物": 0,
        "high_地学基礎": 0,
        "high_地学": 0,
        "high_世界史": 0,
        "high_日本史": 0,
        "high_地理": 0,
        "high_倫理": 0,
        "high_政治経済": 0
    },
    "広瀬駿": {
        "high_国語": 0,
        "high_数学（数学ⅡBまで）": 0,
        "high_数学（数学ⅢCまで）": 0,
        "high_公民": 0,
        "high_英語": 0,
        "high_物理基礎": 0,
        "high_物理": 0,
        "high_化学基礎": 0,
        "high_化学": 0,
        "high_生物基礎": 0,
        "high_生物": 0,
        "high_地学基礎": 0,
        "high_地学": 0,
        "high_世界史": 0,
        "high_日本史": 0,
        "high_地理": 0,
        "high_倫理": 0,
        "high_政治経済": 0
    },
    "萩原悠": {
        "high_国語": 0,
        "high_数学（数学ⅡBまで）": 0,
        "high_数学（数学ⅢCまで）": 0,
        "high_公民": 0,
        "high_英語": 0,
        "high_物理基礎": 0,
        "high_物理": 0,
        "high_化学基礎": 0,
        "high_化学": 0,
        "high_生物基礎": 0,
        "high_生物": 0,
        "high_地学基礎": 0,
        "high_地学": 0,
        "high_世界史": 0,
        "high_日本史": 0,
        "high_地理": 0,
        "high_倫理": 0,
        "high_政治経済": 0
    },
    "桜井智": {
        "high_国語": 0,
        "high_数学（数学ⅡBまで）": 0,
        "high_数学（数学ⅢCまで）": 0,
        "high_公民": 0,
        "high_英語": 0,
        "high_物理基礎": 0,
        "high_物理": 0,
        "high_化学基礎": 0,
        "high_化学": 0,
        "high_生物基礎": 0,
        "high_生物": 0,
        "high_地学基礎": 0,
        "high_地学": 0,
        "high_世界史": 0,
        "high_日本史": 0,
        "high_地理": 0,
        "high_倫理": 0,
        "high_政治経済": 0
    },
    "藤本綾": {
        "high_国語": 0,
        "high_数学（数学ⅡBまで）": 0,
        "high_数学（数学ⅢCまで）": 0,
        "high_公民": 0,
        "high_英語": 0,
        "high_物理基礎": 0,
        "high_物理": 0,
        "high_化学基礎": 0,
        "high_化学": 0,
        "high_生物基礎": 0,
        "high_生物": 0,
        "high_地学基礎": 0,
        "high_地学": 0,
        "high_世界史": 0,
        "high_日本史": 0,
        "high_地理": 0,
        "high_倫理": 0,
        "high_政治経済": 0
    },
    "川端翼": {
        "high_国語": 0,
        "high_数学（数学ⅡBまで）": 0,
        "high_数学（数学ⅢCまで）": 0,
        "high_公民": 0,
        "high_英語": 0,
        "high_物理基礎": 0,
        "high_物理": 0,
        "high_化学基礎": 0,
        "high_化学": 0,
        "high_生物基礎": 0,
        "high_生物": 0,
        "high_地学基礎": 0,
        "high_地学": 0,
        "high_世界史": 0,
        "high_日本史": 0,
        "high_地理": 0,
        "high_倫理": 0,
        "high_政治経済": 0
    },
    "井村悠斗": {
        "high_国語": 0,
        "high_数学（数学ⅡBまで）": 0,
        "high_数学（数学ⅢCまで）": 0,
        "high_公民": 0,
        "high_英語": 0,
        "high_物理基礎": 0,
        "high_物理": 0,
        "high_化学基礎": 0,
        "high_化学": 0,
        "high_生物基礎": 0,
        "high_生物": 0,
        "high_地学基礎": 0,
        "high_地学": 0,
        "high_世界史": 0,
        "high_日本史": 0,
        "high_地理": 0,
        "high_倫理": 0,
        "high_政治経済": 0
    }
}


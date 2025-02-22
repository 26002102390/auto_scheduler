import gspread
from google.oauth2.service_account import Credentials

# ① ダウンロードしたJSONのファイルパス
SERVICE_ACCOUNT_FILE = "/Users/cdl/Desktop/triple-water-451506-t4-df3fab7dcfb4.json"

# ② スコープの設定（読み書き両方の権限を付与）
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# ③ 認証情報の取得
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# ④ Googleスプレッドシートに接続
client = gspread.authorize(creds)

# ⑤ スプレッドシートを開く
SPREADSHEET_URL_teacher = "https://docs.google.com/spreadsheets/d/1LbAfbIY7fhy9HDrYxPut9GMkAiyynTKQwh9o8EmUCBw/edit"
SPREADSHEET_URL_student = "https://docs.google.com/spreadsheets/d/1BWXM3OZwKJs5O-Ib5HuMMRX9HSLWWGy35PdwpE7_yNI/edit"
SPREADSHEET_ID_teacher = SPREADSHEET_URL_teacher.split('/')[5]
SPREADSHEET_ID_student = SPREADSHEET_URL_student.split('/')[5]

sheet_teacher = client.open_by_key(SPREADSHEET_ID_teacher).sheet1
sheet_student = client.open_by_key(SPREADSHEET_ID_student).sheet1

# ⑥ データを取得して整形
all_values_teacher = sheet_teacher.get_all_values()
all_values_student = sheet_student.get_all_values()

headers_teacher = all_values_teacher[0]
data_teacher = all_values_teacher[1:]
headers_student = all_values_student[0]
data_student = all_values_student[1:]

def parse_periods(period_str):
    """時限文字列をパースして辞書形式に変換"""
    periods = {2: False, 3: False, 4: False, 5: False, 6: False}
    if not period_str:
        return periods
    
    # "2限, 3限, 4限" → [2, 3, 4]
    available = [int(p.strip().replace('限', '')) for p in period_str.split(',') if p.strip()]
    
    for p in available:
        if p in periods:
            periods[p] = True
    
    return periods


# print(headers_teacher)
# print(data_teacher)

# 名前をキーとして，他のデータに関する辞書を値とする辞書を作成
teachers_dict = {}
# print(headers_teacher)
for row in data_teacher:
    name = row[2]
    teachers_dict[name] = {
        headers_teacher[i]: row[i] for i in range(len(headers_teacher)) if i != 2
    }

students_dict = {}
for row in data_student:
    name = row[1]
    students_dict[name] = {
        headers_student[i]: row[i] for i in range(len(headers_student)) if i != 1
    }
# print(students_dict)

# 教師の空きコマを辞書に変換
def parse_availability(raw_data):
    availability = {}
    for teacher, data in raw_data.items():
        availability[teacher] = {}
        for date_key in data:
            if date_key.startswith("8/"):
                date_formatted = f"8月{date_key[2:]}日"
                slots = {2: False, 3: False, 4: False, 5: False, 6: False}
                if data[date_key]:
                    for period in data[date_key].split(', '):
                        slot_number = int(period[0])
                        slots[slot_number] = True
                availability[teacher][date_formatted] = slots
    return availability


def parse_can_teach(raw_data):
    subjects = {
        "elementary": {"国語": "国語（小学生）", "算数": "算数（小学生）", "理科": "理科（小学生）", "社会": "社会（小学生）", "英語": "英語（小学生）"},
        "middle": {"国語": "国語（中学生）", "数学": "数学（中学生）", "理科": "理科（中学生）", "社会": "社会（中学生）", "英語": "英語（中学生）"},
        "high": {
            "国語": "国語（高校生）", "数学ⅠA": "数学ⅠA（高校生）", "数学ⅡB": "数学ⅡB（高校生）", "数学ⅢC": "数学ⅢC（高校生）", 
            "英語": "英語（高校生）", "物理基礎": "物理基礎（高校生）", "物理": "物理（高校生）", "化学基礎": "化学基礎（高校生）", "化学": "化学（高校生）", 
            "生物基礎": "生物基礎（高校生）", "生物": "生物（高校生）", "地学基礎": "地学基礎（高校生）", "地学": "地学（高校生）", 
            "世界史": "世界史（高校生）", "日本史": "日本史（高校生）", "地理": "地理（高校生）", "倫理": "倫理（高校生）", "政経": "政経（高校生）"
        }
    }
    can_teach = {}
    
    for teacher, data in raw_data.items():
        can_teach[teacher] = {}
        subjects_list = data["指導可能科目"].split(', ')
        
        for level, sub_dict in subjects.items():
            for sub_key, sub_value in sub_dict.items():
                can_teach[teacher][f"{level}_{sub_key}"] = sub_value in subjects_list
    
    return can_teach


def parse_teachers(raw_data):
    teachers = []
    for teacher, data in raw_data.items():
        teachers.append({
            "name": teacher,
            "min_continuous": 2 if data["最低限出勤コマ数"].isdigit() and int(data["最低限出勤コマ数"]) > 1 else 1,
            "avoid_gaps": data["空きコマに関する質問"].strip() == "空きコマは避けたい"
        })
    return teachers

# 教師の情報を辞書に変換
teachers = parse_teachers(teachers_dict)
# print(teachers)

# 教師の空きコマを辞書に変換
availability = parse_availability(teachers_dict)
# print(availability["test"])

# 教師の指導可能科目を辞書に変換
can_teach = parse_can_teach(teachers_dict)
# print(can_teach["田中先生"])


def parse_student_data(raw_data):
    students = []
    student_availability = {}
    required_lessons = {}
    
    for student, data in raw_data.items():
        school_level = "elementary" if "小学生" in data["所属を選んでください"] else "middle" if "中学生" in data["所属を選んでください"] else "high"
        
        students.append({
            "name": student,
            "school_level": school_level,
            "grade": 1,  # グレード情報がないためデフォルト
            "preference": "continuous" if data["空きコマに関する質問"] == "空きコマは避けたい" else "normal"
        })
        
        # 授業希望コマ
        required_lessons[student] = {}
        valid_subjects = {
            "elementary": ["国語", "算数", "理科", "社会", "英語"],
            "middle": ["国語", "数学", "理科", "社会", "英語"],
            "high": ["国語", "数学ⅠA", "数学ⅡB", "数学ⅢC", "化学基礎", "化学", "物理基礎", "物理", "生物基礎", "生物", "地学基礎", "地学", "地理", "日本史", "世界史", "倫理", "政経", "英語"]
        }
        
        for subject in valid_subjects[school_level]:
            key = f"{data['所属を選んでください']}：受講希望科目 （表を右にスクロールできます） [{subject}]"
            if key in data:
                lesson_count = data[key].replace("コマ", "")
                required_lessons[student][f"{school_level}_{subject}"] = int(lesson_count) if lesson_count.isdigit() else 0
        
        # 授業可能時間
        student_availability[student] = {}
        for day in ["8/1", "8/2", "8/3", "8/4"]:
            formatted_day = f"8月{day[2:]}日"
            slots = {2: False, 3: False, 4: False, 5: False, 6: False}
            
            if f"希望授業枠（表を右にスクロールできます） [{day}]" in data:
                if data[f"希望授業枠（表を右にスクロールできます） [{day}]"]:
                    for period in data[f"希望授業枠（表を右にスクロールできます） [{day}]"].split(', '):
                        slot_number = int(period[0])
                        slots[slot_number] = True
            student_availability[student][formatted_day] = slots
    
    return students, student_availability, required_lessons

# 入力データの処理
students, student_availability, required_lessons = parse_student_data(students_dict)

print(students)
print(student_availability)
print(required_lessons)
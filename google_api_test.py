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
SPREADSHEET_URL_student = "https://docs.google.com/spreadsheets/d/19U6ObgU8qAe7s8wVp3miUGiEotgBCzwS2_BkdkESrrs/edit"
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

# ⑦ teachersデータの形式に変換
teachers = []
for row in data_teacher:
    row_dict = dict(zip(headers_teacher, row))
    
    # 最低連続コマ数を取得（デフォルト値は2）
    min_continuous = int(row_dict['最低限出勤コマ数']) if row_dict['最低限出勤コマ数'] else 2
    
    # 空きコマの設定を取得
    avoid_gaps = row_dict['空きコマに関する質問'] == '空きコマは避けたい'
    
    # 指導可能科目を整形
    subjects = [s.strip() for s in row_dict['指導可能科目'].split(',') if s.strip()]
    
    teacher = {
        "name": row_dict['名前（姓 名）'],
        "min_continuous": min_continuous,
        "avoid_gaps": avoid_gaps,
        "subjects": subjects,  # 追加情報として保持
        "availability": {
            "8月1日": parse_periods(row_dict.get('8/1', '') or row_dict.get('シフト [8/1]', '')),
            "8月2日": parse_periods(row_dict.get('8/2', '') or row_dict.get('シフト [8/2]', '')),
            "8月3日": parse_periods(row_dict.get('8/3', '') or row_dict.get('シフト [8/3]', '')),
            "8月4日": parse_periods(row_dict.get('8/4', '') or row_dict.get('シフト [8/4]', '')),
        }
    }
    teachers.append(teacher)

# 結果の表示
print("\nConverted Teachers Data:")
for teacher in teachers:
    print(f"\n{teacher['name']}:")
    print(f"  最低連続コマ数: {teacher['min_continuous']}")
    print(f"  空きコマ回避: {teacher['avoid_gaps']}")
    print(f"  指導可能科目: {', '.join(teacher['subjects'])}")
    print("  出勤可能時間:")
    for day, periods in teacher['availability'].items():
        available = [str(p) for p, v in periods.items() if v]
        if available:
            print(f"    {day}: {', '.join(available)}限")

# ⑧ studentsデータの形式に変換  
students = []
for row in data_student:
    row_dict = dict(zip(headers_student, row))
    student = {
        "name": row_dict['名前（姓 名）'],
        "school_level": row_dict['学校レベル'],
        "grade": int(row_dict['学年']),
        "preference": row_dict['シフト希望']
    }
    students.append(student)

# 結果の表示
print("\nConverted Students Data:")
for student in students:
    print(f"\n{student['name']}:")
    print(f"  学校レベル: {student['school_level']}")
    print(f"  学年: {student['grade']}")
    print(f"  シフト希望: {student['preference']}")

# # ⑨ データをファイルに保存
# with open('teachers.json', 'w') as f:
#     json.dump(teachers, f, indent=4)

# with open('students.json', 'w') as f:
#     json.dump(students, f, indent=4)

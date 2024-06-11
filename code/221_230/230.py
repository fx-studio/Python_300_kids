# 230 - Viết chương trình để tạo báo cáo dữ liệu đơn giản

#### Định nghĩa hàm đọc dữ liệu
import pandas as pd
import json

def read_csv(file_path):
    return pd.read_csv(file_path)

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
    return pd.DataFrame(data)

def read_excel(file_path):
    return pd.read_excel(file_path)


#### Định nghĩa hàm phân tích dữ liệu
def analyze_data(df):
    report = {}
    report['total_rows'] = len(df)
    report['columns'] = list(df.columns)
    report['summary'] = df.describe(include='all').to_dict()
    return report


#### Định nghĩa hàm tạo báo cáo
def create_report(report):
    report_text = []
    report_text.append(f"Total rows: {report['total_rows']}")
    report_text.append("Columns:")
    for column in report['columns']:
        report_text.append(f" - {column}")
    report_text.append("Summary statistics:")
    for col, stats in report['summary'].items():
        report_text.append(f"Column: {col}")
        for stat, value in stats.items():
            report_text.append(f"  {stat}: {value}")
    return "\n".join(report_text)

#### Định nghĩa hàm chính để tạo báo cáo từ tệp
def generate_report(file_path, file_type):
    if file_type == 'csv':
        df = read_csv(file_path)
    elif file_type == 'json':
        df = read_json(file_path)
    elif file_type == 'excel':
        df = read_excel(file_path)
    else:
        raise ValueError("Unsupported file type")

    report = analyze_data(df)
    report_text = create_report(report)
    return report_text

#### Sử dụng hàm chính để tạo báo cáo
file_path = 'students.csv'  # Thay đổi đường dẫn và kiểu tệp theo nhu cầu
file_type = 'csv'  # 'csv', 'json', hoặc 'excel'

report_text = generate_report(file_path, file_type)
print(report_text)
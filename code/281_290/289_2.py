# 289 - Tạo dữ liệu mẫu và lưu vào tệp CSV, sau đó thực hiện phân tích dữ liệu sử dụng Pandas

import pandas as pd

# Tạo một DataFrame với dữ liệu mẫu
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'A', 'B', 'C'],
    'Value': [10, 20, 15, 10, 25, 30, 5, 40, 35, 10]
}

df = pd.DataFrame(data)

# Lưu DataFrame vào file CSV
df.to_csv('data.csv', index=False)
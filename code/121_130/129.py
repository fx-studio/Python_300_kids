# 129 - Viết chương trình để sử dụng hàm lambda để sắp xếp danh sách từ điển theo giá trị

# Danh sách từ điển cần sắp xếp
dict_list = [{'name': 'John', 'age': 20}, {'name': 'Jane', 'age': 22}, {'name': 'Doe', 'age': 19}]

# Sắp xếp danh sách từ điển theo giá trị của 'age'
sorted_list = sorted(dict_list, key=lambda x: x['age'])

print(f"Danh sách sau khi sắp xếp: {sorted_list}")
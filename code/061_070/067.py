# 067 - Viết chương trình để kiểm tra một chuỗi có chứa một từ không

# Tạo một chuỗi và một từ cần kiểm tra
str1 = "Hello, World!"
word = "World"

# Sử dụng toán tử in
# Kiểm tra xem chuỗi có chứa từ cần kiểm tra không
contains_word = word in str1
print(contains_word)

# Sử dụng phương thức find()
# Kiểm tra xem chuỗi có chứa từ cần kiểm tra không
contains_word = str1.find(word) != -1
print(contains_word)
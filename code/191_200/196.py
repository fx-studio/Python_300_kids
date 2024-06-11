# 196 - Viết chương trình để tạo một generator sinh ra các chuỗi từ một danh sách các từ

def word_generator(word_list):
    for word in word_list:
        yield word

# Sử dụng generator
word_list = ["apple", "banana", "cherry", "date", "elderberry"]
word_gen = word_generator(word_list)

# Duyệt qua các phần tử bằng next
for _ in range(len(word_list)):
    print(next(word_gen))
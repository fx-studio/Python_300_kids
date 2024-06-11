# 049 - Viết chương trình để đếm số lượng cặp key-value trong dictionary

# Khởi tạo một dictionary với các cặp key-value ban đầu
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# In dictionary ban đầu
print("Dictionary ban đầu:", my_dict)

# Phương pháp 1: Sử dụng hàm len() trực tiếp trên dictionary
count1 = len(my_dict)
print("Số lượng cặp key-value (Phương pháp 1):", count1)

# Phương pháp 2: Sử dụng phương thức items() và hàm len()
count2 = len(my_dict.items())
print("Số lượng cặp key-value (Phương pháp 2):", count2)

# Phương pháp 3: Sử dụng vòng lặp for để đếm thủ công
count3 = 0
for _ in my_dict:
    count3 += 1
print("Số lượng cặp key-value (Phương pháp 3):", count3)

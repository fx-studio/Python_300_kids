# 184 - Viết chương trình để lặp qua một iterator

# Định nghĩa một danh sách
my_collection = [1, 2, 3, 4, 5]

# Tạo một iterator từ danh sách
my_iterator = iter(my_collection)

# Phương pháp 1: Sử dụng vòng lặp for
print("Using for loop:")
for element in my_iterator:
    print(element)

# Reset lại iterator cho các phương pháp khác
my_iterator = iter(my_collection)

# Phương pháp 2: Sử dụng list comprehension
print("\nUsing list comprehension:")
elements = [element for element in my_iterator]
print(elements)

# Reset lại iterator cho các phương pháp khác
my_iterator = iter(my_collection)

# Phương pháp 3: Sử dụng hàm list() để chuyển iterator thành list
print("\nUsing list() function:")
elements = list(my_iterator)
print(elements)

# Reset lại iterator cho các phương pháp khác
my_iterator = iter(my_collection)

# Phương pháp 4: Sử dụng hàm itertools.islice() để lặp qua các phần tử
import itertools
print("\nUsing itertools.islice():")
for element in itertools.islice(my_iterator, 0, None):
    print(element)

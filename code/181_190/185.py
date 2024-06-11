# 185 - Viết chương trình để sử dụng hàm next() để truy cập các phần tử của một iterator

# Định nghĩa một danh sách
my_collection = [1, 2, 3, 4, 5]

# Tạo một iterator từ danh sách
my_iterator = iter(my_collection)

# Sử dụng vòng lặp while và hàm next() để duyệt qua các phần tử của iterator
while True:
    try:
        # Lấy phần tử tiếp theo từ iterator
        element = next(my_iterator)
        print(element)
    except StopIteration:
        # Nếu không còn phần tử nào trong iterator thì thoát khỏi vòng lặp
        break
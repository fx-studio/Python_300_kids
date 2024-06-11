# 181 - Viết chương trình để tạo một iterator từ một list

# Định nghĩa một danh sách
my_list = [1, 2, 3, 4, 5]

# Tạo một iterator từ danh sách
my_iterator = iter(my_list)

# Sử dụng vòng lặp để duyệt qua các phần tử của iterator
while True:
    try:
        # Lấy phần tử tiếp theo từ iterator
        element = next(my_iterator)
        print(element)
    except StopIteration:
        # Nếu không còn phần tử nào trong iterator thì thoát khỏi vòng lặp
        break

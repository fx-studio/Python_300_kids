# 052 - Viết chương trình để thêm một phần tử vào set

# Khởi tạo một set ban đầu
my_set = {'apple', 'banana', 'cherry'}
print("Set ban đầu:", my_set)

# Phương pháp 1: Sử dụng phương thức add() để thêm một phần tử vào set
my_set.add('orange')
print("Set sau khi thêm 'orange' bằng phương thức add():", my_set)

# Phương pháp 2: Sử dụng phương thức update() để thêm một phần tử vào set
my_set.update(['grape'])  # Phương thức update() nhận vào một iterable, vì vậy phần tử cần được đưa vào một iterable
print("Set sau khi thêm 'grape' bằng phương thức update():", my_set)

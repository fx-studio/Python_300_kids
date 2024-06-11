# 053 - Viết chương trình để xóa một phần tử khỏi set

# Khởi tạo một set ban đầu
my_set = {'apple', 'banana', 'cherry'}
print("Set ban đầu:", my_set)

# Phương pháp 1: Sử dụng phương thức remove() để xóa một phần tử khỏi set
my_set.remove('banana')
print("Set sau khi xóa 'banana' bằng phương thức remove():", my_set)

# Phương pháp 2: Sử dụng phương thức discard() để xóa một phần tử khỏi set
my_set.discard('apple')
print("Set sau khi xóa 'apple' bằng phương thức discard():", my_set)
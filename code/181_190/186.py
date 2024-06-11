# 186 - Viết chương trình để tạo một iterator tùy chỉnh

class CustomIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# Sử dụng iterator tùy chỉnh với một danh sách
my_data = [10, 20, 30, 40, 50]
my_iterator = CustomIterator(my_data)

# Duyệt qua các phần tử của iterator tùy chỉnh bằng vòng lặp for
for element in my_iterator:
    print(element)
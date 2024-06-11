# 180 - Viết chương trình để tạo một decorator sử dụng hàm generator

def generator_decorator(func):
    def inner(*args, **kwargs):
        yield from func(*args, **kwargs)
    return inner

@generator_decorator
def count_up_to(n):
    return (i for i in range(1, n+1))

# Get the generator
print(list(count_up_to(5)))  # Output: [1, 2, 3, 4, 5]

# Print the numbers
for num in count_up_to(5):
    print(num)  # Output: 1, 2, 3, 4, 5
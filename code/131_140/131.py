# 131 - Viết chương trình để tính dãy Fibonacci

# Cách 1: Sử dụng vòng lặp for
def fibonacci_for(n):
    """
    Hàm để tính dãy Fibonacci sử dụng vòng lặp for.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibo_seq = [0, 1]
    for i in range(2, n):
        next_fibo = fibo_seq[-1] + fibo_seq[-2]
        fibo_seq.append(next_fibo)
    
    return fibo_seq

# Số lượng phần tử Fibonacci cần tính
n = 10

# Gọi hàm và in kết quả
fibo_seq = fibonacci_for(n)
print("Dãy Fibonacci sử dụng vòng lặp for:", fibo_seq)

# Cách 2: Sử dụng đệ quy
def fibonacci_recursive(n):
    """
    Hàm đệ quy để tính số Fibonacci tại vị trí n.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_sequence_recursive(n):
    """
    Hàm để tạo dãy Fibonacci sử dụng đệ quy.
    """
    return [fibonacci_recursive(i) for i in range(n)]

# Số lượng phần tử Fibonacci cần tính
n = 10

# Gọi hàm và in kết quả
fibo_seq = fibonacci_sequence_recursive(n)
print("Dãy Fibonacci sử dụng đệ quy:", fibo_seq)

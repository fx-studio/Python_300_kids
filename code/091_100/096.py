## 096 - Viết chương trình để tự định nghĩa ngoại lệ

class CustomException(Exception):
    """
    Đây là một lớp ngoại lệ tùy chỉnh.

    Lớp này được sử dụng để đại diện cho một ngoại lệ tùy chỉnh trong Python. 
    Khi một ngoại lệ tùy chỉnh được ném ra, chương trình sẽ dừng lại và xử lý ngoại lệ này theo cách mà người dùng mong muốn.

    Trong trường hợp này, từ khóa 'pass' được sử dụng để không thực hiện bất kỳ hành động nào trong lớp ngoại lệ này.
    Nó chỉ đơn giản là để đảm bảo rằng lớp ngoại lệ không có bất kỳ phương thức hoặc thuộc tính nào khác ngoài việc kế thừa từ lớp Exception.
    """

    pass

def raise_custom_exception():
    try:
        raise CustomException("This is a custom exception!")
    except CustomException as e:
        print(e)

raise_custom_exception()
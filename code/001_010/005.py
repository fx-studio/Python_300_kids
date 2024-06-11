# 005 - Viết chương trình để tính điểm trung bình và xếp loại học sinh.

# Hàm tính toán
def calculate_average(scores):
    return sum(scores) / len(scores)

# Hàm phân loại
def classify_student(average):
    if average >= 8.5:
        return "Xuất sắc"
    elif average >= 7.0:
        return "Giỏi"
    elif average >= 5.5:
        return "Khá"
    elif average >= 4.0:
        return "Trung bình"
    else:
        return "Yếu"

# Nhập điểm số từ người dùng
try:
    scores = []
    num_subjects = int(input("Nhập số lượng môn học: "))
    if num_subjects <= 0:
        print("Số lượng môn học phải lớn hơn 0.")
    else:
        for i in range(num_subjects):
            score = float(input(f"Nhập điểm môn học thứ {i+1}: "))
            if score < 0 or score > 10:
                print("Điểm số phải từ 0 đến 10. Vui lòng nhập lại.")
                break
            scores.append(score)
        
        if len(scores) == num_subjects:
            average_score = calculate_average(scores)
            classification = classify_student(average_score)
            print(f"Điểm trung bình: {average_score:.2f}")
            print(f"Xếp loại: {classification}")
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")
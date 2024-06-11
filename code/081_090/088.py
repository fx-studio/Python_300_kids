# 088 - Viết chương trình để ghi đè phương thức của lớp cha

# Định nghĩa lớp cơ bản Nguoi
class Nguoi:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi
    
    def hien_thi_thong_tin(self):
        print(f"Tên: {self.ten}")
        print(f"Tuổi: {self.tuoi}")

# Định nghĩa lớp HocSinh kế thừa từ lớp Nguoi
class HocSinh(Nguoi):
    def __init__(self, ten, tuoi, lop, diem_tb):
        super().__init__(ten, tuoi)
        self.lop = lop
        self.diem_tb = diem_tb
    
    def hien_thi_thong_tin(self):
        # Sử dụng phương thức của lớp cha để hiển thị tên và tuổi
        super().hien_thi_thong_tin()
        # Thêm thông tin về lớp và điểm trung bình
        print(f"Lớp: {self.lop}")
        print(f"Điểm trung bình: {self.diem_tb}")

# Tạo đối tượng từ lớp HocSinh
hs = HocSinh("Nguyễn Văn A", 16, "10A1", 8.2)

# Gọi phương thức hien_thi_thong_tin của đối tượng HocSinh
hs.hien_thi_thong_tin()

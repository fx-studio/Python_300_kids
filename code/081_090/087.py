# 087 - Viết chương trình để kế thừa từ một lớp cơ bản

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
        super().hien_thi_thong_tin()
        print(f"Lớp: {self.lop}")
        print(f"Điểm trung bình: {self.diem_tb}")
    
    def xep_loai(self):
        if self.diem_tb >= 8.5:
            return "Giỏi"
        elif self.diem_tb >= 6.5:
            return "Khá"
        elif self.diem_tb >= 5.0:
            return "Trung bình"
        else:
            return "Yếu"

# Tạo đối tượng từ lớp HocSinh
hs = HocSinh("Nguyễn Văn A", 16, "10A1", 8.2)

# Gọi các phương thức
hs.hien_thi_thong_tin()
print(f"Xếp loại: {hs.xep_loai()}")

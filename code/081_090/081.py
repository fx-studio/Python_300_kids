# 081 - Viết chương trình để tạo một lớp học sinh

class HocSinh:
    def __init__(self, ten, tuoi, diem_tb):
        """Phương thức khởi tạo để thiết lập các thuộc tính của học sinh"""
        self.ten = ten
        self.tuoi = tuoi
        self.diem_tb = diem_tb
    
    def hien_thi_thong_tin(self):
        """Phương thức để hiển thị thông tin của học sinh"""
        print(f"Học sinh: {self.ten}")
        print(f"Tuổi: {self.tuoi}")
        print(f"Điểm trung bình: {self.diem_tb}")
    
    def xep_loai(self):
        """Phương thức để xếp loại học sinh dựa trên điểm trung bình"""
        if self.diem_tb >= 8.5:
            return "Giỏi"
        elif self.diem_tb >= 6.5:
            return "Khá"
        elif self.diem_tb >= 5.0:
            return "Trung bình"
        else:
            return "Yếu"

# Tạo đối tượng học sinh
hs = HocSinh("Nguyễn Văn A", 16, 8.2)

# Hiển thị thông tin học sinh
hs.hien_thi_thong_tin()

# Xếp loại học sinh
print(f"Xếp loại: {hs.xep_loai()}")

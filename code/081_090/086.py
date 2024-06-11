# 086 - Viết chương trình để gọi phương thức của đối tượng

class HocSinh:
    def __init__(self, ten, tuoi, diem_tb, dia_chi):
        """Phương thức khởi tạo để thiết lập các thuộc tính của học sinh"""
        self.ten = ten
        self.tuoi = tuoi
        self.diem_tb = diem_tb
        self.dia_chi = dia_chi
    
    def hien_thi_thong_tin(self):
        """Phương thức public để hiển thị thông tin của học sinh"""
        print(f"Học sinh: {self.ten}")
        print(f"Tuổi: {self.tuoi}")
        print(f"Điểm trung bình: {self.diem_tb}")
        print(f"Địa chỉ: {self.dia_chi}")
        self.__xep_loai()  # Gọi phương thức private từ phương thức public
    
    def xep_loai(self):
        """Phương thức public để xếp loại học sinh dựa trên điểm trung bình"""
        if self.diem_tb >= 8.5:
            return "Giỏi"
        elif self.diem_tb >= 6.5:
            return "Khá"
        elif self.diem_tb >= 5.0:
            return "Trung bình"
        else:
            return "Yếu"

    def __xep_loai(self):
        """Phương thức private để xếp loại học sinh dựa trên điểm trung bình"""
        loai = self.xep_loai()
        print(f"Xếp loại: {loai}")

# Tạo đối tượng học sinh
hs = HocSinh("Nguyễn Văn A", 16, 8.2, "123 Đường A, Thành phố B")

# Gọi phương thức public của đối tượng
hs.hien_thi_thong_tin()

# Gọi phương thức private thông qua phương thức public
# Note: Không thể gọi phương thức private trực tiếp từ bên ngoài
# hs.__xep_loai()  # Sẽ gây lỗi AttributeError

# 083 - Viết chương trình để thêm phương thức cho lớp học sinh

class HocSinh:
    def __init__(self, ten, tuoi, diem_tb, dia_chi):
        """Phương thức khởi tạo để thiết lập các thuộc tính của học sinh"""
        self.ten = ten
        self.tuoi = tuoi
        self.diem_tb = diem_tb
        self.dia_chi = dia_chi
    
    def hien_thi_thong_tin(self):
        """Phương thức để hiển thị thông tin của học sinh"""
        print(f"Học sinh: {self.ten}")
        print(f"Tuổi: {self.tuoi}")
        print(f"Điểm trung bình: {self.diem_tb}")
        print(f"Địa chỉ: {self.dia_chi}")
    
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
    
    # Phương thức được thêm mới
    def cap_nhat_diem(self, diem_moi):
        """Phương thức để cập nhật điểm trung bình của học sinh"""
        self.diem_tb = diem_moi
        print(f"Điểm trung bình mới của học sinh {self.ten} là: {self.diem_tb}")

    def loi_chao(self):
        """Phương thức để hiển thị lời chào từ học sinh"""
        print(f"Xin chào! Tôi là {self.ten} và tôi học lớp 12. Rất vui được gặp bạn!")

# Tạo đối tượng học sinh với thuộc tính địa chỉ
hs = HocSinh("Nguyễn Văn A", 16, 8.2, "123 Đường A, Thành phố B")

# Hiển thị thông tin học sinh
hs.hien_thi_thong_tin()

# Xếp loại học sinh
print(f"Xếp loại: {hs.xep_loai()}")

# Cập nhật điểm trung bình và hiển thị thông tin
hs.cap_nhat_diem(9.0)

# Hiển thị lời chào từ học sinh
hs.loi_chao()

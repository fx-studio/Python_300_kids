# 084 - Viết chương trình để tạo đối tượng từ lớp học sinh

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

# Tạo đối tượng học sinh
hs1 = HocSinh("Nguyễn Văn A", 16, 8.2, "123 Đường A, Thành phố B")
hs2 = HocSinh("Trần Thị B", 15, 7.5, "456 Đường B, Thành phố C")
hs3 = HocSinh("Lê Văn C", 17, 9.0, "789 Đường C, Thành phố D")

# Tạo danh sách các đối tượng học sinh
danh_sach_hoc_sinh = [hs1, hs2, hs3]

# Hiển thị thông tin của từng học sinh trong danh sách
for hoc_sinh in danh_sach_hoc_sinh:
    hoc_sinh.hien_thi_thong_tin()
    print(f"Xếp loại: {hoc_sinh.xep_loai()}")
    print("-----")

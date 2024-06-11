# 085 - Viết chương trình để truy cập thuộc tính của đối tượng

class HocSinh:
    def __init__(self, ten, tuoi, diem_tb, dia_chi):
        """Phương thức khởi tạo để thiết lập các thuộc tính của học sinh"""
        self.ten = ten  # Thuộc tính public
        self._tuoi = tuoi  # Thuộc tính private
        self.diem_tb = diem_tb  # Thuộc tính public
        self.__dia_chi = dia_chi  # Thuộc tính private (name mangling)
    
    def hien_thi_thong_tin(self):
        """Phương thức để hiển thị thông tin của học sinh"""
        print(f"Học sinh: {self.ten}")
        print(f"Tuổi: {self._tuoi}")
        print(f"Điểm trung bình: {self.diem_tb}")
        print(f"Địa chỉ: {self.__dia_chi}")
    
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
    
    # Getter cho thuộc tính private _tuoi
    @property
    def tuoi(self):
        return self._tuoi

    # Setter cho thuộc tính private _tuoi
    @tuoi.setter
    def tuoi(self, tuoi_moi):
        if tuoi_moi > 0:
            self._tuoi = tuoi_moi
        else:
            print("Tuổi không hợp lệ!")

    # Getter cho thuộc tính private __dia_chi
    def get_dia_chi(self):
        return self.__dia_chi

    # Setter cho thuộc tính private __dia_chi
    def set_dia_chi(self, dia_chi_moi):
        self.__dia_chi = dia_chi_moi

# Tạo đối tượng học sinh
hs = HocSinh("Nguyễn Văn A", 16, 8.2, "123 Đường A, Thành phố B")

# Truy cập và thay đổi giá trị các thuộc tính public
print(f"Trước khi thay đổi: Tên - {hs.ten}, Điểm trung bình - {hs.diem_tb}")
hs.ten = "Trần Thị B"
hs.diem_tb = 9.0
print(f"Sau khi thay đổi: Tên - {hs.ten}, Điểm trung bình - {hs.diem_tb}")

# Truy cập và thay đổi giá trị các thuộc tính private qua getter và setter
print(f"Trước khi thay đổi: Tuổi - {hs.tuoi}, Địa chỉ - {hs.get_dia_chi()}")
hs.tuoi = 17
hs.set_dia_chi("456 Đường B, Thành phố C")
print(f"Sau khi thay đổi: Tuổi - {hs.tuoi}, Địa chỉ - {hs.get_dia_chi()}")

# Hiển thị thông tin học sinh
hs.hien_thi_thong_tin()

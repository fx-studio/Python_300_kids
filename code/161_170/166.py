# 166 - Viết chương trình để quản lý lịch học

# Định nghĩa một lớp MonHoc với các thuộc tính:
# - ten: tên môn học
# - ma_mon_hoc: mã môn học
class MonHoc:
    def __init__(self, ten, ma_mon_hoc):
        self.ten = ten
        self.ma_mon_hoc = ma_mon_hoc

    def __str__(self):
        return f"Môn học: {self.ten}, Mã môn học: {self.ma_mon_hoc}"

# Định nghĩa một lớp LopHoc với các thuộc tính:
# - mon_hoc: môn học
# - thoi_gian: thời gian học
# - phong_hoc: phòng học
class LopHoc:
    def __init__(self, mon_hoc, thoi_gian, phong_hoc):
        self.mon_hoc = mon_hoc
        self.thoi_gian = thoi_gian
        self.phong_hoc = phong_hoc

    def __str__(self):
        return f"Lớp học: {self.mon_hoc.ten}, Thời gian: {self.thoi_gian}, Phòng học: {self.phong_hoc}"

# Định nghĩa một lớp QuanLyLichHoc với các phương thức:
# - them_mon_hoc: thêm một môn học vào danh sách
# - tao_lop_hoc: tạo một lớp học mới
# - hien_thi_lich_hoc: hiển thị lịch học
# - tim_mon_hoc: tìm môn học theo mã môn học
class QuanLyLichHoc:
    def __init__(self):
        self.danh_sach_mon_hoc = []
        self.danh_sach_lop_hoc = []

    def them_mon_hoc(self, mon_hoc):
        self.danh_sach_mon_hoc.append(mon_hoc)

    def tao_lop_hoc(self, ma_mon_hoc, thoi_gian, phong_hoc):
        mon_hoc = self.tim_mon_hoc(ma_mon_hoc)
        if mon_hoc:
            lop_hoc = LopHoc(mon_hoc, thoi_gian, phong_hoc)
            self.danh_sach_lop_hoc.append(lop_hoc)
            return True
        return False

    def hien_thi_lich_hoc(self):
        for lop_hoc in self.danh_sach_lop_hoc:
            print(lop_hoc)

    def tim_mon_hoc(self, ma_mon_hoc):
        for mon_hoc in self.danh_sach_mon_hoc:
            if mon_hoc.ma_mon_hoc == ma_mon_hoc:
                return mon_hoc
        return None

# Hàm menu để chạy chương trình
def menu():
    qllh = QuanLyLichHoc()
    while True:
        print("\n=====================================")
        print("1. Thêm môn học")
        print("2. Tạo lớp học")
        print("3. Hiển thị lịch học")
        print("4. Thoát")
        lua_chon = input("Chọn một tùy chọn: ")
        print("============== Kết quả ===============")
        
        if lua_chon == '1':
            ten = input("Nhập tên môn học: ")
            ma_mon_hoc = input("Nhập mã môn học: ")
            mon_hoc = MonHoc(ten, ma_mon_hoc)
            qllh.them_mon_hoc(mon_hoc)
            print("Đã thêm môn học.")
        
        elif lua_chon == '2':
            ma_mon_hoc = input("Nhập mã môn học: ")
            thoi_gian = input("Nhập thời gian học: ")
            phong_hoc = input("Nhập phòng học: ")
            if qllh.tao_lop_hoc(ma_mon_hoc, thoi_gian, phong_hoc):
                print("Đã tạo lớp học.")
            else:
                print("Không tìm thấy môn học.")
        
        elif lua_chon == '3':
            qllh.hien_thi_lich_hoc()
        
        elif lua_chon == '4':
            print("Thoát chương trình.")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    menu()

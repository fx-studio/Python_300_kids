# 161 - Viết chương trình để quản lý danh sách học sinh

# Định nghĩa một lớp HocSinh với các thuộc tính:
# - ten: tên học sinh
# - tuoi: tuổi học sinh
# - lop: lớp học sinh
class HocSinh:
    def __init__(self, ten, tuoi, lop):
        self.ten = ten
        self.tuoi = tuoi
        self.lop = lop

    def __str__(self):
        return f"Học sinh: {self.ten}, Tuổi: {self.tuoi}, Lớp: {self.lop}"

# Định nghĩa một lớp QuanLyHocSinh với các phương thức:
# - them_hoc_sinh: thêm một học sinh vào danh sách
# - xoa_hoc_sinh: xóa một học sinh khỏi danh sách
# - hien_thi_danh_sach: hiển thị danh sách học sinh
class QuanLyHocSinh:
    def __init__(self):
        self.danh_sach_hoc_sinh = []

    def them_hoc_sinh(self, hoc_sinh):
        self.danh_sach_hoc_sinh.append(hoc_sinh)

    def xoa_hoc_sinh(self, ten):
        for hoc_sinh in self.danh_sach_hoc_sinh:
            if hoc_sinh.ten == ten:
                self.danh_sach_hoc_sinh.remove(hoc_sinh)
                return True
        return False

    def hien_thi_danh_sach(self):
        print("Danh sách học sinh:")
        for hoc_sinh in self.danh_sach_hoc_sinh:
            print(hoc_sinh)

# Hàm menu để chạy chương trình
def menu():
    qlhs = QuanLyHocSinh()
    while True:
        print("=====================================")
        print("1. Thêm học sinh")
        print("2. Xóa học sinh")
        print("3. Hiển thị danh sách học sinh")
        print("4. Thoát")
        lua_chon = input("Chọn một tùy chọn: ")
        print("=====================================")

        if lua_chon == '1':
            ten = input("Nhập tên học sinh: ")
            tuoi = input("Nhập tuổi học sinh: ")
            lop = input("Nhập lớp học sinh: ")
            hoc_sinh = HocSinh(ten, tuoi, lop)
            qlhs.them_hoc_sinh(hoc_sinh)
            print("Đã thêm học sinh.")

        elif lua_chon == '2':
            ten = input("Nhập tên học sinh cần xóa: ")
            if qlhs.xoa_hoc_sinh(ten):
                print("Đã xóa học sinh.")
            else:
                print("Không tìm thấy học sinh.")

        elif lua_chon == '3':
            qlhs.hien_thi_danh_sach()

        elif lua_chon == '4':
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        
if __name__ == "__main__":
    menu()
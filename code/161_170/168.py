# 168 - Viết chương trình để quản lý thông tin cá nhân

# Định nghĩa một lớp ThongTinCaNhan với các thuộc tính:
# - ten: tên
# - tuoi: tuổi
# - dia_chi: địa chỉ
# - so_dien_thoai: số điện thoại
# - email: email
# 
# Các phương thức:
# - cap_nhat(ten, tuoi, dia_chi, so_dien_thoai, email): cập nhật thông tin cá nhân
class ThongTinCaNhan:
    def __init__(self, ten, tuoi, dia_chi, so_dien_thoai, email):
        self.ten = ten
        self.tuoi = tuoi
        self.dia_chi = dia_chi
        self.so_dien_thoai = so_dien_thoai
        self.email = email

    def cap_nhat(self, ten=None, tuoi=None, dia_chi=None, so_dien_thoai=None, email=None):
        if ten is not None:
            self.ten = ten
        if tuoi is not None:
            self.tuoi = tuoi
        if dia_chi is not None:
            self.dia_chi = dia_chi
        if so_dien_thoai is not None:
            self.so_dien_thoai = so_dien_thoai
        if email is not None:
            self.email = email

    def __str__(self):
        return (f"Tên: {self.ten}, Tuổi: {self.tuoi}, Địa chỉ: {self.dia_chi}, "
                f"Số điện thoại: {self.so_dien_thoai}, Email: {self.email}")

# Định nghĩa một lớp QuanLyThongTinCaNhan với các phương thức:
# - them_thong_tin(thong_tin): thêm thông tin cá nhân
# - cap_nhat_thong_tin(ten, ten_moi, tuoi, dia_chi, so_dien_thoai, email): cập nhật thông tin cá nhân
# - hien_thi_thong_tin(ten): hiển thị thông tin cá nhân
class QuanLyThongTinCaNhan:
    def __init__(self):
        self.danh_sach_thong_tin = []

    def them_thong_tin(self, thong_tin):
        self.danh_sach_thong_tin.append(thong_tin)

    def cap_nhat_thong_tin(self, ten, ten_moi=None, tuoi=None, dia_chi=None, so_dien_thoai=None, email=None):
        for thong_tin in self.danh_sach_thong_tin:
            if thong_tin.ten == ten:
                thong_tin.cap_nhat(ten=ten_moi, tuoi=tuoi, dia_chi=dia_chi, so_dien_thoai=so_dien_thoai, email=email)
                return True
        return False

    def hien_thi_thong_tin(self, ten):
        for thong_tin in self.danh_sach_thong_tin:
            if thong_tin.ten == ten:
                print(thong_tin)
                return
        print("Không tìm thấy thông tin cá nhân.")

# Hàm menu để hiển thị menu và xử lý tùy chọn
def menu():
    qlttcn = QuanLyThongTinCaNhan()
    while True:
        print("=====================================")
        print("1. Thêm thông tin cá nhân")
        print("2. Cập nhật thông tin cá nhân")
        print("3. Hiển thị thông tin cá nhân")
        print("4. Thoát")
        lua_chon = input("Chọn một tùy chọn: ")
        print("============== Kết quả ===============")
        
        if lua_chon == '1':
            ten = input("Nhập tên: ")
            tuoi = int(input("Nhập tuổi: "))
            dia_chi = input("Nhập địa chỉ: ")
            so_dien_thoai = input("Nhập số điện thoại: ")
            email = input("Nhập email: ")
            thong_tin = ThongTinCaNhan(ten, tuoi, dia_chi, so_dien_thoai, email)
            qlttcn.them_thong_tin(thong_tin)
            print("Đã thêm thông tin cá nhân.")
        
        elif lua_chon == '2':
            ten = input("Nhập tên của thông tin cá nhân cần cập nhật: ")
            ten_moi = input("Nhập tên mới (hoặc nhấn Enter để giữ nguyên): ")
            tuoi = input("Nhập tuổi mới (hoặc nhấn Enter để giữ nguyên): ")
            dia_chi = input("Nhập địa chỉ mới (hoặc nhấn Enter để giữ nguyên): ")
            so_dien_thoai = input("Nhập số điện thoại mới (hoặc nhấn Enter để giữ nguyên): ")
            email = input("Nhập email mới (hoặc nhấn Enter để giữ nguyên): ")
            tuoi = int(tuoi) if tuoi else None
            cap_nhat_thanh_cong = qlttcn.cap_nhat_thong_tin(ten, ten_moi=ten_moi, tuoi=tuoi, dia_chi=dia_chi, so_dien_thoai=so_dien_thoai, email=email)
            if cap_nhat_thanh_cong:
                print("Đã cập nhật thông tin cá nhân.")
            else:
                print("Không tìm thấy thông tin cá nhân.")
        
        elif lua_chon == '3':
            ten = input("Nhập tên của thông tin cá nhân cần hiển thị: ")
            qlttcn.hien_thi_thong_tin(ten)
        
        elif lua_chon == '4':
            print("Thoát chương trình.")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    menu()

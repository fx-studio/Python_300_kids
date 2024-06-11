# 165 - Viết chương trình để quản lý nhân viên

# Định nghĩa một lớp NhanVien với các thuộc tính:
# - ten: tên nhân viên
# - tuoi: tuổi nhân viên
# - vi_tri: vị trí công việc của nhân viên
class NhanVien:
    def __init__(self, ten, tuoi, vi_tri):
        self.ten = ten
        self.tuoi = tuoi
        self.vi_tri = vi_tri
        self.phong_ban = None

    # Phương thức __str__ trả về thông tin của nhân viên
    def __str__(self):
        phong_ban = self.phong_ban.ten if self.phong_ban else "Chưa có"
        return f"Nhân viên: {self.ten}, Tuổi: {self.tuoi}, Vị trí: {self.vi_tri}, Phòng ban: {phong_ban}"

# Định nghĩa một lớp PhongBan với các thuộc tính:
# - ten: tên phòng ban
# - danh_sach_nhan_vien: danh sách nhân viên trong phòng ban
class PhongBan:
    def __init__(self, ten):
        self.ten = ten
        self.danh_sach_nhan_vien = []

    def them_nhan_vien(self, nhan_vien):
        self.danh_sach_nhan_vien.append(nhan_vien)
        nhan_vien.phong_ban = self

    # Phương thức __str__ trả về thông tin của phòng ban
    def __str__(self):
        nhan_vien_str = ', '.join(nv.ten for nv in self.danh_sach_nhan_vien)
        return f"Phòng ban: {self.ten}, Nhân viên: {nhan_vien_str}"

# Định nghĩa một lớp QuanLyNhanSu với các phương thức:
# - them_nhan_vien: thêm một nhân viên vào danh sách
# - them_phong_ban: thêm một phòng ban vào danh sách
# - gan_nhan_vien_vao_phong_ban: gán một nhân viên vào một phòng ban
# - hien_thi_danh_sach_nhan_vien: hiển thị danh sách nhân viên
# - hien_thi_danh_sach_phong_ban: hiển thị danh sách phòng ban
# - tim_nhan_vien: tìm nhân viên theo tên
# - tim_phong_ban: tìm phòng ban theo tên
class QuanLyNhanSu:
    def __init__(self):
        self.danh_sach_nhan_vien = []
        self.danh_sach_phong_ban = []

    def them_nhan_vien(self, nhan_vien):
        self.danh_sach_nhan_vien.append(nhan_vien)

    def them_phong_ban(self, phong_ban):
        self.danh_sach_phong_ban.append(phong_ban)

    def gan_nhan_vien_vao_phong_ban(self, ten_nhan_vien, ten_phong_ban):
        nhan_vien = self.tim_nhan_vien(ten_nhan_vien)
        phong_ban = self.tim_phong_ban(ten_phong_ban)
        if nhan_vien and phong_ban:
            phong_ban.them_nhan_vien(nhan_vien)
            return True
        return False

    def hien_thi_danh_sach_nhan_vien(self):
        for nhan_vien in self.danh_sach_nhan_vien:
            print(nhan_vien)

    def hien_thi_danh_sach_phong_ban(self):
        for phong_ban in self.danh_sach_phong_ban:
            print(phong_ban)

    def tim_nhan_vien(self, ten):
        for nhan_vien in self.danh_sach_nhan_vien:
            if nhan_vien.ten == ten:
                return nhan_vien
        return None

    def tim_phong_ban(self, ten):
        for phong_ban in self.danh_sach_phong_ban:
            if phong_ban.ten == ten:
                return phong_ban
        return None

# Hàm menu để chạy chương trình
def menu():
    qlns = QuanLyNhanSu()
    while True:
        print("\n=====================================")
        print("1. Thêm nhân viên")
        print("2. Thêm phòng ban")
        print("3. Gán nhân viên vào phòng ban")
        print("4. Hiển thị danh sách nhân viên")
        print("5. Hiển thị danh sách phòng ban")
        print("6. Thoát")
        lua_chon = input("Chọn một tùy chọn: ")
        print("============== Kết quả ===============")
        
        if lua_chon == '1':
            ten = input("Nhập tên nhân viên: ")
            tuoi = int(input("Nhập tuổi nhân viên: "))
            vi_tri = input("Nhập vị trí công việc của nhân viên: ")
            nhan_vien = NhanVien(ten, tuoi, vi_tri)
            qlns.them_nhan_vien(nhan_vien)
            print("Đã thêm nhân viên.")
        
        elif lua_chon == '2':
            ten = input("Nhập tên phòng ban: ")
            phong_ban = PhongBan(ten)
            qlns.them_phong_ban(phong_ban)
            print("Đã thêm phòng ban.")
        
        elif lua_chon == '3':
            ten_nhan_vien = input("Nhập tên nhân viên: ")
            ten_phong_ban = input("Nhập tên phòng ban: ")
            if qlns.gan_nhan_vien_vao_phong_ban(ten_nhan_vien, ten_phong_ban):
                print("Đã gán nhân viên vào phòng ban.")
            else:
                print("Không thể gán nhân viên vào phòng ban.")
        
        elif lua_chon == '4':
            qlns.hien_thi_danh_sach_nhan_vien()
        
        elif lua_chon == '5':
            qlns.hien_thi_danh_sach_phong_ban()
        
        elif lua_chon == '6':
            print("Thoát chương trình.")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    menu()

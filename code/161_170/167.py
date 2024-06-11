# 167 - Viết chương trình để quản lý điểm thi

# Định nghĩa một lớp SinhVien với các thuộc tính:
# - ten: tên sinh viên
# - ma_sv: mã sinh viên
class SinhVien:
    def __init__(self, ten, ma_sv):
        self.ten = ten
        self.ma_sv = ma_sv

    def __str__(self):
        return f"Sinh viên: {self.ten}, Mã sinh viên: {self.ma_sv}"

# Định nghĩa một lớp MonHoc với các thuộc tính:
# - ten: tên môn học
# - ma_mh: mã môn học
class MonHoc:
    def __init__(self, ten, ma_mh):
        self.ten = ten
        self.ma_mh = ma_mh

    def __str__(self):
        return f"Môn học: {self.ten}, Mã môn học: {self.ma_mh}"

# Định nghĩa một lớp KyThi với các thuộc tính:
# - ten: tên kỳ thi
# - ma_ky_thi: mã kỳ thi
class KyThi:
    def __init__(self, ten, ma_ky_thi):
        self.ten = ten
        self.ma_ky_thi = ma_ky_thi

    def __str__(self):
        return f"Kỳ thi: {self.ten}, Mã kỳ thi: {self.ma_ky_thi}"

# Định nghĩa một lớp DiemThi với các thuộc tính:
# - sinh_vien: sinh viên
# - mon_hoc: môn học
# - ky_thi: kỳ thi
# - diem: điểm thi
class DiemThi:
    def __init__(self, sinh_vien, mon_hoc, ky_thi, diem):
        self.sinh_vien = sinh_vien
        self.mon_hoc = mon_hoc
        self.ky_thi = ky_thi
        self.diem = diem

    def __str__(self):
        return f"Sinh viên: {self.sinh_vien.ten}, Môn học: {self.mon_hoc.ten}, Kỳ thi: {self.ky_thi.ten}, Điểm: {self.diem}"

# Định nghĩa một lớp QuanLyDiemThi với các phương thức:
# - them_sinh_vien: thêm một sinh viên vào danh sách
# - them_mon_hoc: thêm một môn học vào danh sách
# - them_ky_thi: thêm một kỳ thi vào danh sách
# - ghi_diem: ghi điểm cho một sinh viên
class QuanLyDiemThi:
    def __init__(self):
        self.danh_sach_sinh_vien = []
        self.danh_sach_mon_hoc = []
        self.danh_sach_ky_thi = []
        self.danh_sach_diem_thi = []

    def them_sinh_vien(self, sinh_vien):
        self.danh_sach_sinh_vien.append(sinh_vien)

    def them_mon_hoc(self, mon_hoc):
        self.danh_sach_mon_hoc.append(mon_hoc)

    def them_ky_thi(self, ky_thi):
        self.danh_sach_ky_thi.append(ky_thi)

    def ghi_diem(self, ma_sv, ma_mh, ma_ky_thi, diem):
        sinh_vien = self.tim_sinh_vien(ma_sv)
        mon_hoc = self.tim_mon_hoc(ma_mh)
        ky_thi = self.tim_ky_thi(ma_ky_thi)
        if sinh_vien and mon_hoc and ky_thi:
            diem_thi = DiemThi(sinh_vien, mon_hoc, ky_thi, diem)
            self.danh_sach_diem_thi.append(diem_thi)
            return True
        return False

    def hien_thi_diem_thi(self, ma_sv):
        sinh_vien = self.tim_sinh_vien(ma_sv)
        if sinh_vien:
            for diem_thi in self.danh_sach_diem_thi:
                if diem_thi.sinh_vien == sinh_vien:
                    print(diem_thi)
        else:
            print("Không tìm thấy sinh viên.")

    def tim_sinh_vien(self, ma_sv):
        for sinh_vien in self.danh_sach_sinh_vien:
            if sinh_vien.ma_sv == ma_sv:
                return sinh_vien
        return None

    def tim_mon_hoc(self, ma_mh):
        for mon_hoc in self.danh_sach_mon_hoc:
            if mon_hoc.ma_mh == ma_mh:
                return mon_hoc
        return None

    def tim_ky_thi(self, ma_ky_thi):
        for ky_thi in self.danh_sach_ky_thi:
            if ky_thi.ma_ky_thi == ma_ky_thi:
                return ky_thi
        return None

# Hàm menu để chạy chương trình
def menu():
    qldt = QuanLyDiemThi()
    while True:
        print("=====================================")
        print("1. Thêm sinh viên")
        print("2. Thêm môn học")
        print("3. Thêm kỳ thi")
        print("4. Ghi điểm thi")
        print("5. Hiển thị điểm thi của sinh viên")
        print("6. Thoát")
        lua_chon = input("Chọn một tùy chọn: ")
        print("============== Kết quả ===============")
        
        if lua_chon == '1':
            ten = input("Nhập tên sinh viên: ")
            ma_sv = input("Nhập mã sinh viên: ")
            sinh_vien = SinhVien(ten, ma_sv)
            qldt.them_sinh_vien(sinh_vien)
            print("Đã thêm sinh viên.")
        
        elif lua_chon == '2':
            ten = input("Nhập tên môn học: ")
            ma_mh = input("Nhập mã môn học: ")
            mon_hoc = MonHoc(ten, ma_mh)
            qldt.them_mon_hoc(mon_hoc)
            print("Đã thêm môn học.")
        
        elif lua_chon == '3':
            ten = input("Nhập tên kỳ thi: ")
            ma_ky_thi = input("Nhập mã kỳ thi: ")
            ky_thi = KyThi(ten, ma_ky_thi)
            qldt.them_ky_thi(ky_thi)
            print("Đã thêm kỳ thi.")
        
        elif lua_chon == '4':
            ma_sv = input("Nhập mã sinh viên: ")
            ma_mh = input("Nhập mã môn học: ")
            ma_ky_thi = input("Nhập mã kỳ thi: ")
            diem = float(input("Nhập điểm thi: "))
            if qldt.ghi_diem(ma_sv, ma_mh, ma_ky_thi, diem):
                print("Đã ghi điểm.")
            else:
                print("Không thể ghi điểm (không tìm thấy sinh viên, môn học hoặc kỳ thi).")
        
        elif lua_chon == '5':
            ma_sv = input("Nhập mã sinh viên: ")
            qldt.hien_thi_diem_thi(ma_sv)
        
        elif lua_chon == '6':
            print("Thoát chương trình.")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    menu()

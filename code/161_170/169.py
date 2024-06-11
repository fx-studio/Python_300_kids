# 169 - Viết chương trình để quản lý thu chi cá nhân

# Định nghĩa một lớp GiaoDich với các thuộc tính:
# - so_tien: số tiền
# - loai: loại giao dịch (thu/chi)
# - mo_ta: mô tả giao dịch
class GiaoDich:
    def __init__(self, so_tien, loai, mo_ta):
        self.so_tien = so_tien
        self.loai = loai
        self.mo_ta = mo_ta

    def __str__(self):
        return f"Số tiền: {self.so_tien}, Loại: {self.loai}, Mô tả: {self.mo_ta}"

# Định nghĩa một lớp Thang với các thuộc tính:
# - thang: tháng
# - danh_sach_giao_dich: danh sách giao dịch trong tháng
#
# Các phương thức:
# - them_giao_dich(giao_dich): thêm một giao dịch vào danh sách
# - hien_thi_thu_chi(): hiển thị thông tin thu chi của tháng
class Thang:
    def __init__(self, thang):
        self.thang = thang
        self.danh_sach_giao_dich = []

    def them_giao_dich(self, giao_dich):
        self.danh_sach_giao_dich.append(giao_dich)

    def hien_thi_thu_chi(self):
        print(f"----- Tháng {self.thang} -----")
        for giao_dich in self.danh_sach_giao_dich:
            print(giao_dich)

# Định nghĩa một lớp QuanLyThuChi với các phương thức:
# - them_thang(thang): thêm một tháng vào danh sách
# - them_giao_dich(thang, giao_dich): thêm một giao dịch vào tháng
# - hien_thi_thu_chi_theo_thang(thang): hiển thị thông tin thu chi của tháng
class QuanLyThuChi:
    def __init__(self):
        self.danh_sach_thang = {}

    def them_thang(self, thang):
        self.danh_sach_thang[thang] = Thang(thang)

    def them_giao_dich(self, thang, giao_dich):
        if thang in self.danh_sach_thang:
            self.danh_sach_thang[thang].them_giao_dich(giao_dich)
            return True
        return False

    def hien_thi_thu_chi_theo_thang(self, thang):
        if thang in self.danh_sach_thang:
            self.danh_sach_thang[thang].hien_thi_thu_chi()
        else:
            print("Không có dữ liệu cho tháng này.")

# Hàm menu để chạy chương trình
def menu():
    qltc = QuanLyThuChi()
    while True:
        print("====== Quản lý thu chi cá nhân =======")
        print("1. Thêm thông tin thu chi cho một tháng")
        print("2. Hiển thị thông tin thu chi của một tháng")
        print("3. Thoát")
        lua_chon = input("Chọn một tùy chọn: ")
        print("============== Kết quả ===============")

        if lua_chon == '1':
            thang = input("Nhập tháng (vd: 01, 02, ..., 12): ")
            if thang not in qltc.danh_sach_thang:
                qltc.them_thang(thang)
            loai_gd = input("Nhập loại giao dịch (thu/chi): ")
            so_tien = float(input("Nhập số tiền: "))
            mo_ta = input("Nhập mô tả: ")
            giao_dich = GiaoDich(so_tien, loai_gd, mo_ta)
            if qltc.them_giao_dich(thang, giao_dich):
                print("Đã thêm thông tin thu chi.")
            else:
                print("Lỗi: Tháng không tồn tại.")

        elif lua_chon == '2':
            thang = input("Nhập tháng để hiển thị thông tin thu chi: ")
            qltc.hien_thi_thu_chi_theo_thang(thang)

        elif lua_chon == '3':
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    menu()

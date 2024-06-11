# 164 - Viết chương trình để quản lý kho hàng

# Định nghĩa một lớp HangHoa với các thuộc tính:
# - ten: tên hàng hóa
# - gia: giá hàng hóa
# - so_luong: số lượng tồn kho
class HangHoa:
    def __init__(self, ten, gia, so_luong):
        self.ten = ten
        self.gia = gia
        self.so_luong = so_luong

    def __str__(self):
        return f"Hàng hóa: {self.ten}, Giá: {self.gia}, Số lượng tồn kho: {self.so_luong}"

# Định nghĩa một lớp QuanLyKho với các phương thức:
# - them_hang_hoa: thêm một hàng hóa vào danh sách
# - nhap_hang: nhập hàng vào kho
# - xuat_hang: xuất hàng từ kho
# - hien_thi_danh_sach_hang_hoa: hiển thị danh sách hàng hóa
# - tim_hang_hoa: tìm hàng hóa theo tên
class QuanLyKho:
    def __init__(self):
        self.danh_sach_hang_hoa = []

    def them_hang_hoa(self, hang_hoa):
        self.danh_sach_hang_hoa.append(hang_hoa)

    def nhap_hang(self, ten, so_luong):
        hang_hoa = self.tim_hang_hoa(ten)
        if hang_hoa:
            hang_hoa.so_luong += so_luong
            return True
        return False

    def xuat_hang(self, ten, so_luong):
        hang_hoa = self.tim_hang_hoa(ten)
        if hang_hoa and hang_hoa.so_luong >= so_luong:
            hang_hoa.so_luong -= so_luong
            return True
        return False

    def hien_thi_danh_sach_hang_hoa(self):
        for hang_hoa in self.danh_sach_hang_hoa:
            print(hang_hoa)

    def tim_hang_hoa(self, ten):
        for hang_hoa in self.danh_sach_hang_hoa:
            if hang_hoa.ten == ten:
                return hang_hoa
        return None

# Hàm menu để chạy chương trình
def menu():
    qlk = QuanLyKho()
    while True:
        print("\n=====================================")
        print("1. Thêm hàng hóa")
        print("2. Nhập hàng")
        print("3. Xuất hàng")
        print("4. Hiển thị danh sách hàng hóa")
        print("5. Thoát")
        lua_chon = input("Chọn một tùy chọn: ")
        print("============== Kết quả ===============")
        
        if lua_chon == '1':
            ten = input("Nhập tên hàng hóa: ")
            gia = float(input("Nhập giá hàng hóa: "))
            so_luong = int(input("Nhập số lượng tồn kho: "))
            hang_hoa = HangHoa(ten, gia, so_luong)
            qlk.them_hang_hoa(hang_hoa)
            print("Đã thêm hàng hóa.")
        
        elif lua_chon == '2':
            ten = input("Nhập tên hàng hóa cần nhập: ")
            so_luong = int(input("Nhập số lượng cần nhập: "))
            if qlk.nhap_hang(ten, so_luong):
                print("Đã nhập hàng.")
            else:
                print("Không tìm thấy hàng hóa.")
        
        elif lua_chon == '3':
            ten = input("Nhập tên hàng hóa cần xuất: ")
            so_luong = int(input("Nhập số lượng cần xuất: "))
            if qlk.xuat_hang(ten, so_luong):
                print("Đã xuất hàng.")
            else:
                print("Không thể xuất hàng (không đủ số lượng hoặc không tìm thấy hàng hóa).")
        
        elif lua_chon == '4':
            qlk.hien_thi_danh_sach_hang_hoa()
        
        elif lua_chon == '5':
            print("Thoát chương trình.")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    menu()

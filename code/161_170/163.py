# 163 - Viết chương trình để quản lý cửa hàng bán lẻ

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

# Định nghĩa một lớp DonHang với các thuộc tính:
# - danh_sach_hang_hoa: danh sách hàng hóa trong đơn hàng
# - tong_tien: tổng tiền của đơn hàng
class DonHang:
    def __init__(self):
        self.danh_sach_hang_hoa = []
        self.tong_tien = 0

    def them_hang_hoa(self, hang_hoa, so_luong):
        if hang_hoa.so_luong >= so_luong:
            self.danh_sach_hang_hoa.append((hang_hoa, so_luong))
            hang_hoa.so_luong -= so_luong
            self.tong_tien += hang_hoa.gia * so_luong
            return True
        return False

    def __str__(self):
        danh_sach = ", ".join(f"{hang_hoa.ten} (x{so_luong})" for hang_hoa, so_luong in self.danh_sach_hang_hoa)
        return f"Đơn hàng: {danh_sach}, Tổng tiền: {self.tong_tien}"

# Định nghĩa một lớp QuanLyCuaHang với các phương thức:
# - them_hang_hoa: thêm một hàng hóa vào danh sách
# - tao_don_hang: tạo một đơn hàng từ danh sách hàng hóa
# - hien_thi_danh_sach_hang_hoa: hiển thị danh sách hàng hóa
# - hien_thi_danh_sach_don_hang: hiển thị danh sách đơn hàng
# - tim_hang_hoa: tìm hàng hóa theo tên
class QuanLyCuaHang:
    def __init__(self):
        self.danh_sach_hang_hoa = []
        self.danh_sach_don_hang = []

    def them_hang_hoa(self, hang_hoa):
        self.danh_sach_hang_hoa.append(hang_hoa)

    def tao_don_hang(self, danh_sach_mua_hang):
        don_hang = DonHang()
        for ten_hang_hoa, so_luong in danh_sach_mua_hang.items():
            hang_hoa = self.tim_hang_hoa(ten_hang_hoa)
            if hang_hoa:
                if not don_hang.them_hang_hoa(hang_hoa, so_luong):
                    print(f"Không đủ số lượng hàng hóa: {ten_hang_hoa}")
                    return None
        self.danh_sach_don_hang.append(don_hang)
        return don_hang

    def hien_thi_danh_sach_hang_hoa(self):
        for hang_hoa in self.danh_sach_hang_hoa:
            print(hang_hoa)

    def hien_thi_danh_sach_don_hang(self):
        for don_hang in self.danh_sach_don_hang:
            print(don_hang)

    def tim_hang_hoa(self, ten):
        for hang_hoa in self.danh_sach_hang_hoa:
            if hang_hoa.ten == ten:
                return hang_hoa
        return None

# Hàm menu để chạy chương trình
def menu():
    qlch = QuanLyCuaHang()
    while True:
        print("=====================================")
        print("1. Thêm hàng hóa")
        print("2. Tạo đơn hàng")
        print("3. Hiển thị danh sách hàng hóa")
        print("4. Hiển thị danh sách đơn hàng")
        print("5. Thoát")
        lua_chon = input("Chọn một tùy chọn: ")
        print("============== Kết quả ===============")
        
        if lua_chon == '1':
            ten = input("Nhập tên hàng hóa: ")
            gia = float(input("Nhập giá hàng hóa: "))
            so_luong = int(input("Nhập số lượng tồn kho: "))
            hang_hoa = HangHoa(ten, gia, so_luong)
            qlch.them_hang_hoa(hang_hoa)
            print("Đã thêm hàng hóa.")
        
        elif lua_chon == '2':
            danh_sach_mua_hang = {}
            while True:
                ten = input("Nhập tên hàng hóa cần mua (hoặc 'xong' để kết thúc): ")
                if ten == 'xong':
                    break
                so_luong = int(input("Nhập số lượng: "))
                danh_sach_mua_hang[ten] = so_luong
            don_hang = qlch.tao_don_hang(danh_sach_mua_hang)
            if don_hang:
                print("Đã tạo đơn hàng.")
            else:
                print("Không thể tạo đơn hàng.")
        
        elif lua_chon == '3':
            qlch.hien_thi_danh_sach_hang_hoa()
        
        elif lua_chon == '4':
            qlch.hien_thi_danh_sach_don_hang()
        
        elif lua_chon == '5':
            print("Thoát chương trình.")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    menu()

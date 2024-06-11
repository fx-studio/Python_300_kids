# 170 - Viết chương trình để quản lý công việc hàng ngày

# Định nghĩa một lớp CongViec với các thuộc tính:
# - ten: tên công việc
# - mo_ta: mô tả công việc
# - hoan_thanh: trạng thái hoàn thành công việc (mặc định là False)
class CongViec:
    def __init__(self, ten, mo_ta, hoan_thanh=False):
        self.ten = ten
        self.mo_ta = mo_ta
        self.hoan_thanh = hoan_thanh

    def cap_nhat(self, ten=None, mo_ta=None, hoan_thanh=None):
        if ten is not None:
            self.ten = ten
        if mo_ta is not None:
            self.mo_ta = mo_ta
        if hoan_thanh is not None:
            self.hoan_thanh = hoan_thanh

    def __str__(self):
        trang_thai = "Hoàn thành" if self.hoan_thanh else "Chưa hoàn thành"
        return f"Tên công việc: {self.ten}, Mô tả: {self.mo_ta}, Trạng thái: {trang_thai}"

# Định nghĩa một lớp QuanLyCongViec với các phương thức:
# - them_cong_viec: thêm một công việc vào danh sách
# - cap_nhat_cong_viec: cập nhật thông tin công việc
# - xoa_cong_viec: xóa một công việc khỏi danh sách
# - hien_thi_danh_sach_cong_viec: hiển thị danh sách công việc
class QuanLyCongViec:
    def __init__(self):
        self.danh_sach_cong_viec = []

    def them_cong_viec(self, cong_viec):
        self.danh_sach_cong_viec.append(cong_viec)

    def cap_nhat_cong_viec(self, ten, ten_moi=None, mo_ta=None, hoan_thanh=None):
        for cv in self.danh_sach_cong_viec:
            if cv.ten == ten:
                cv.cap_nhat(ten=ten_moi, mo_ta=mo_ta, hoan_thanh=hoan_thanh)
                return True
        return False

    def xoa_cong_viec(self, ten):
        for cv in self.danh_sach_cong_viec:
            if cv.ten == ten:
                self.danh_sach_cong_viec.remove(cv)
                return True
        return False

    def hien_thi_danh_sach_cong_viec(self):
        if not self.danh_sach_cong_viec:
            print("Không có công việc nào.")
        else:
            for cv in self.danh_sach_cong_viec:
                print(cv)

# Hàm menu để chạy chương trình
def menu():
    qlcv = QuanLyCongViec()
    while True:
        print("\n----- Quản lý công việc hàng ngày -----")
        print("1. Thêm công việc mới")
        print("2. Chỉnh sửa công việc")
        print("3. Xóa công việc")
        print("4. Hiển thị danh sách công việc")
        print("5. Thoát")
        lua_chon = input("Chọn một tùy chọn: ")
        print("--------------- Kết quả ---------------")

        if lua_chon == '1':
            ten = input("Nhập tên công việc: ")
            mo_ta = input("Nhập mô tả công việc: ")
            cong_viec = CongViec(ten, mo_ta)
            qlcv.them_cong_viec(cong_viec)
            print("Đã thêm công việc mới.")

        elif lua_chon == '2':
            ten = input("Nhập tên công việc cần chỉnh sửa: ")
            ten_moi = input("Nhập tên mới (hoặc nhấn Enter để giữ nguyên): ")
            mo_ta_moi = input("Nhập mô tả mới (hoặc nhấn Enter để giữ nguyên): ")
            hoan_thanh = input("Công việc đã hoàn thành? (yes/no): ")
            hoan_thanh = True if hoan_thanh.lower() == "yes" else False
            cap_nhat_thanh_cong = qlcv.cap_nhat_cong_viec(ten, ten_moi=ten_moi, mo_ta=mo_ta_moi, hoan_thanh=hoan_thanh)
            if cap_nhat_thanh_cong:
                print("Đã cập nhật công việc.")
            else:
                print("Không tìm thấy công việc.")

        elif lua_chon == '3':
            ten = input("Nhập tên công việc cần xóa: ")
            xoa_thanh_cong = qlcv.xoa_cong_viec(ten)
            if xoa_thanh_cong:
                print("Đã xóa công việc.")
            else:
                print("Không tìm thấy công việc.")

        elif lua_chon == '4':
            print("Danh sách công việc:")
            qlcv.hien_thi_danh_sach_cong_viec()

        elif lua_chon == '5':
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    menu()

# 162 - Viết chương trình để quản lý thư viện sách

# Định nghĩa một lớp Sach với các thuộc tính:
# - tieu_de: tiêu đề sách
# - tac_gia: tác giả sách
# - da_muon: trạng thái sách đã mượn hay chưa
class Sach:
    def __init__(self, tieu_de, tac_gia):
        self.tieu_de = tieu_de
        self.tac_gia = tac_gia
        self.da_muon = False

    def __str__(self):
        trang_thai = "Đã mượn" if self.da_muon else "Chưa mượn"
        return f"Sách: {self.tieu_de}, Tác giả: {self.tac_gia}, Trạng thái: {trang_thai}"

# Định nghĩa một lớp NguoiMuon với các thuộc tính:
# - ten: tên người mượn
# - danh_sach_sach_muon: danh sách sách mà người mượn đã mượn
class NguoiMuon:
    def __init__(self, ten):
        self.ten = ten
        self.danh_sach_sach_muon = []

    def muon_sach(self, sach):
        if not sach.da_muon:
            self.danh_sach_sach_muon.append(sach)
            sach.da_muon = True
            return True
        return False

    def tra_sach(self, tieu_de):
        for sach in self.danh_sach_sach_muon:
            if sach.tieu_de == tieu_de:
                self.danh_sach_sach_muon.remove(sach)
                sach.da_muon = False
                return True
        return False

    def __str__(self):
        danh_sach = ", ".join(sach.tieu_de for sach in self.danh_sach_sach_muon)
        return f"Người mượn: {self.ten}, Sách đã mượn: {danh_sach}"

# Định nghĩa một lớp QuanLyThuVien với phương thức:
# - them_sach: thêm một sách vào danh sách
# - them_nguoi_muon: thêm một người mượn vào danh sách
# - muon_sach: mượn sách cho một người mượn
# - tra_sach: trả sách cho một người mượn
# - hien_thi_danh_sach_sach: hiển thị danh sách sách
# - hien_thi_danh_sach_nguoi_muon: hiển thị danh sách người mượn
# - tim_sach: tìm sách theo tiêu đề
# - tim_nguoi_muon: tìm người mượn theo tên
class QuanLyThuVien:
    def __init__(self):
        self.danh_sach_sach = []
        self.danh_sach_nguoi_muon = []

    def them_sach(self, sach):
        self.danh_sach_sach.append(sach)

    def them_nguoi_muon(self, nguoi_muon):
        self.danh_sach_nguoi_muon.append(nguoi_muon)

    def muon_sach(self, ten_nguoi_muon, tieu_de_sach):
        nguoi_muon = self.tim_nguoi_muon(ten_nguoi_muon)
        sach = self.tim_sach(tieu_de_sach)
        if nguoi_muon and sach:
            return nguoi_muon.muon_sach(sach)
        return False

    def tra_sach(self, ten_nguoi_muon, tieu_de_sach):
        nguoi_muon = self.tim_nguoi_muon(ten_nguoi_muon)
        if nguoi_muon:
            return nguoi_muon.tra_sach(tieu_de_sach)
        return False

    def hien_thi_danh_sach_sach(self):
        for sach in self.danh_sach_sach:
            print(sach)

    def hien_thi_danh_sach_nguoi_muon(self):
        for nguoi_muon in self.danh_sach_nguoi_muon:
            print(nguoi_muon)

    def tim_sach(self, tieu_de):
        for sach in self.danh_sach_sach:
            if sach.tieu_de == tieu_de:
                return sach
        return None

    def tim_nguoi_muon(self, ten):
        for nguoi_muon in self.danh_sach_nguoi_muon:
            if nguoi_muon.ten == ten:
                return nguoi_muon
        return None

# Hàm menu để chạy chương trình
def menu():
    qltv = QuanLyThuVien()
    while True:
        print("=====================================")
        print("1. Thêm sách")
        print("2. Thêm người mượn")
        print("3. Mượn sách")
        print("4. Trả sách")
        print("5. Hiển thị danh sách sách")
        print("6. Hiển thị danh sách người mượn")
        print("7. Thoát")
        lua_chon = input("Chọn một tùy chọn: ")
        print("=====================================")
        
        if lua_chon == '1':
            tieu_de = input("Nhập tiêu đề sách: ")
            tac_gia = input("Nhập tác giả sách: ")
            sach = Sach(tieu_de, tac_gia)
            qltv.them_sach(sach)
            print("Đã thêm sách.")
        
        elif lua_chon == '2':
            ten = input("Nhập tên người mượn: ")
            nguoi_muon = NguoiMuon(ten)
            qltv.them_nguoi_muon(nguoi_muon)
            print("Đã thêm người mượn.")
        
        elif lua_chon == '3':
            ten = input("Nhập tên người mượn: ")
            tieu_de = input("Nhập tiêu đề sách cần mượn: ")
            if qltv.muon_sach(ten, tieu_de):
                print("Đã mượn sách.")
            else:
                print("Không thể mượn sách.")
        
        elif lua_chon == '4':
            ten = input("Nhập tên người mượn: ")
            tieu_de = input("Nhập tiêu đề sách cần trả: ")
            if qltv.tra_sach(ten, tieu_de):
                print("Đã trả sách.")
            else:
                print("Không thể trả sách.")
        
        elif lua_chon == '5':
            qltv.hien_thi_danh_sach_sach()
        
        elif lua_chon == '6':
            qltv.hien_thi_danh_sach_nguoi_muon()
        
        elif lua_chon == '7':
            print("Thoát chương trình.")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    menu()

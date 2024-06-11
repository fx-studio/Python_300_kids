# 001 - Viết chương trình để kiểm tra số nguyên dương hay âm.

so = int(input("Nhập một số: "))

if so > 0:
    print("Số dương")
elif so == 0:
    print("Số không")
else:
    print("Số âm")
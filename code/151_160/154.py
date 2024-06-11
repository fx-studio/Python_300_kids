# 154 - Viết chương trình để thêm nhãn vào cửa sổ GUI

import tkinter as tk

def change_label_text():
    label.config(text="Nội dung nhãn đã được thay đổi")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Fx Studio")

# Tạo nhãn
label = tk.Label(window, text="Đây là nhãn ban đầu")
label.pack()

# Tạo nút và liên kết với hàm change_label_text
button = tk.Button(window, text="Nhấn để thay đổi nhãn", command=change_label_text)
button.pack()

# Chạy vòng lặp chính của Tkinter
window.mainloop()

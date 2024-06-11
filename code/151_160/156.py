# 165 - Viết chương trình để thêm hộp thoại thông báo vào cửa sổ GUI

import tkinter as tk
from tkinter import messagebox

def clear_textbox():
    textbox.delete("1.0", tk.END)
    messagebox.showinfo("Thông báo", "Nội dung đã được xóa")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Fx Studio")
window.minsize(500, 400)

# Tạo hộp thoại thông báo (Text widget)
textbox = tk.Text(window, width=50, height=10)
textbox.pack(pady=20)

# Tạo nút để xóa nội dung của hộp thoại
clear_button = tk.Button(window, text="Xóa nội dung", command=clear_textbox)
clear_button.pack(pady=20)

# Chạy vòng lặp chính của Tkinter
window.mainloop()

# 155 - Viết chương trình để thêm menu vào cửa sổ GUI

import tkinter as tk
from tkinter import Menu

def show_selected(option):
    label.config(text=f"Bạn đã chọn: {option}")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Fx Studio")

# Tạo nhãn
label = tk.Label(window, text="Chọn một mục từ menu")
label.pack()

# Tạo menu
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Tạo menu chính
main_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=main_menu)

# Thêm các mục vào menu chính
main_menu.add_command(label="Tùy chọn 1", command=lambda: show_selected("Tùy chọn 1"))
main_menu.add_command(label="Tùy chọn 2", command=lambda: show_selected("Tùy chọn 2"))
main_menu.add_command(label="Tùy chọn 3", command=lambda: show_selected("Tùy chọn 3"))

# Chạy vòng lặp chính của Tkinter
window.mainloop()

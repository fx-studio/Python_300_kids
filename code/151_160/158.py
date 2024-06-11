# 158 - Viết chương trình để thêm bảng vào cửa sổ GUI

import tkinter as tk
from tkinter import ttk
import random

def add_random_data():
    data = [str(random.randint(1, 100)) for _ in range(3)]
    tree.insert("", "end", values=data)

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Fx Studio")
window.minsize(600, 400)

# Tạo frame để chứa bảng và thanh cuộn
frame = tk.Frame(window)
frame.pack(fill="both", expand=True)

# Tạo bảng (Treeview)
columns = ("col1", "col2", "col3")
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading("col1", text="Column 1")
tree.heading("col2", text="Column 2")
tree.heading("col3", text="Column 3")

# Tạo thanh cuộn cho bảng
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)

# Tạo nút để thêm dữ liệu ngẫu nhiên vào bảng
add_button = tk.Button(window, text="Thêm dữ liệu ngẫu nhiên", command=add_random_data)
add_button.pack(pady=10)

# Chạy vòng lặp chính của Tkinter
window.mainloop()

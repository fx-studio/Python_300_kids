# 159 - Viết chương trình để thêm đồ thị vào cửa sổ GUI

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Dữ liệu giả về nhiệt độ và lượng mưa trong 12 tháng
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperature = [5, 7, 12, 17, 20, 25, 30, 28, 22, 18, 10, 6]
rainfall = [50, 40, 60, 80, 70, 50, 30, 40, 60, 80, 70, 50]

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Fx Studio")
window.minsize(600, 400)

# Tạo figure và axes cho đồ thị
fig, ax1 = plt.subplots()

# Vẽ dữ liệu nhiệt độ và lượng mưa
ax1.plot(months, temperature, 'r-', label='Temperature (°C)')
ax1.set_xlabel('Month')
ax1.set_ylabel('Temperature (°C)', color='r')
ax2 = ax1.twinx()
ax2.plot(months, rainfall, 'b-', label='Rainfall (mm)')
ax2.set_ylabel('Rainfall (mm)', color='b')

# Thêm legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Tạo canvas để nhúng đồ thị vào Tkinter
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Chạy vòng lặp chính của Tkinter
window.mainloop()

# 157 - Viết chương trình để thêm hình ảnh vào cửa sổ GUI

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
    if file_path:
        load_image(file_path)

def load_image(file_path):
    global image_label  # Declare image_label as global at the start of the function

    img = Image.open(file_path)
    img = img.resize((400, 400), Image.LANCZOS)  # Resize image to fit the window
    img_tk = ImageTk.PhotoImage(img)
    
    if 'image_label' in globals():
        image_label.config(image=img_tk)
        image_label.image = img_tk
    else:
        image_label = tk.Label(window, image=img_tk)
        image_label.image = img_tk
        image_label.pack()

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Fx Studio")
window.minsize(400, 400)

# Tạo nút để mở hộp thoại chọn ảnh
open_button = tk.Button(window, text="Chọn ảnh", command=open_image)
open_button.pack(pady=20)

# Chạy vòng lặp chính của Tkinter
window.mainloop()

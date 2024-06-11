# 152 - Viết chương trình để thêm nút vào cửa sổ GUI

import tkinter as tk

def handle_button_click():
    print("Button clicked!")

root = tk.Tk()
root.title("Fx Studio")
button = tk.Button(root, text="Click me!", command=handle_button_click)
button.pack()
root.mainloop()
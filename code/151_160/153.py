# 153 - Viết chương trình để thêm hộp văn bản vào cửa sổ GUI

import tkinter as tk

def clear_text():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Fx Studio")
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Clear text", command=clear_text)
button.pack()
root.mainloop()
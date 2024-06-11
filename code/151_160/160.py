# 160 - Viết chương trình để tạo ứng dụng máy tính đơn giản với GUI

import tkinter as tk

def click_button(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except Exception as e:
        input_text.set("error")
        expression = ""

# Khởi tạo cửa sổ chính
window = tk.Tk()
window.title("Máy tính đơn giản")
window.geometry("600x300")

expression = ""
input_text = tk.StringVar()

# Tạo khung cho màn hình hiển thị
input_frame = tk.Frame(window, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=tk.TOP)

# Tạo màn hình hiển thị
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT, fg="black")
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Tạo khung cho các nút
btns_frame = tk.Frame(window, width=400, height=450, bg="grey")
btns_frame.pack()

# Định nghĩa các nút
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('=', 4, 2), ('C', 4, 0),
]

# Thêm các nút vào khung
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(btns_frame, text=text, width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: calculate())
    elif text == "C":
        btn = tk.Button(btns_frame, text=text, width=10, height=3, bd=0, bg="#f44336", cursor="hand2", command=lambda: clear())
    else:
        btn = tk.Button(btns_frame, text=text, width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda text=text: click_button(text))
    
    btn.grid(row=row, column=col, padx=1, pady=1)
    btn.config(font=('arial', 14, 'bold'))  # Add this line to make the text bold

# Chạy vòng lặp chính của Tkinter
window.mainloop()

import tkinter as tk
import math
from tkinterweb import HtmlFrame 

root = tk.Tk()
root.title("Calc+br")
root.geometry("480x700") 
root.configure(bg="#0f172a",relief="sunken")

expression = ""

browser_frame = HtmlFrame(root)

def go_back():
    """Hides browser and brings back the calculator UI"""
    browser_frame.pack_forget()
    back_btn.pack_forget()
    entry.pack(fill="x", ipady=12, padx=10, pady=8)
    label.pack(pady=4)
    main_frame.pack(fill="both", expand=True, padx=10, pady=5)

back_btn = tk.Button(root, text="← Back to Calculator", command=go_back, 
                     bg="#ef4444", fg="white", font=("Arial", 10, "bold"), relief="flat")

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    text = equation.get()
    
    try:
        if "." in text and not any(op in text for op in ["+", "-", "*", "/", ","]):
            if not (text.startswith("http://") or text.startswith("https://")):
                text = "https://" + text
            
            entry.pack_forget()
            label.pack_forget()
            main_frame.pack_forget()
            
            back_btn.pack(pady=5, anchor="nw", padx=10)
            browser_frame.pack(fill="both", expand=True)
            browser_frame.load_website(text)
        
        else:
            result = str(eval(expression))
            equation.set(result)
            expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def log_func():
    global expression
    try:
        result = str(math.log(float(expression)))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def power():
    global expression
    try:
        base, exp = expression.split(",")
        result = str(math.pow(float(base), float(exp)))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def mod():
    global expression
    try:
        a, b = expression.split(",")
        result = str(float(a) % float(b))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

equation = tk.StringVar()

entry = tk.Entry(root,
                  textvariable=equation,
                  font=("Consolas", 22),
                  bg="#020617",
                  fg="#38bdf8",
                  bd=2,
                  border="#b51acd",
                  insertwidth=4,
                  justify="center")
entry.pack(fill="x", ipady=12, padx=10, pady=8)

label = tk.Label(root,
    text="Designed By:Arpit Mehrotra, SAP-ID: 590021974",
    bg="#0f172a", fg="white", font=("Times", 11))
label.pack(pady=4)

main_frame = tk.Frame(root, bg="#0f172a")
main_frame.pack(fill="both", expand=True, padx=10, pady=5)

for i in range(6):
    main_frame.rowconfigure(i, weight=1, uniform="row")

for j in range(4):
    main_frame.columnconfigure(j, weight=1, uniform="col")

btn_color = "#e5e7eb"
op_color = "#6b7280"
equal_color = "#22c55e"

def create_button(text, row, col, cmd, bg):
    tk.Button(main_frame,
              text=text,
              command=cmd,
              bg=bg,
              fg="black" if bg != equal_color else "white",
              font=("Arial", 14, "bold"),
              relief="flat"
    ).grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('C',4,2), ('+',4,3)
]

for (text,row,col) in buttons:
    if text == 'C':
        create_button(text, row, col, clear, "#ef4444")
    elif text in ['+','-','*','/']:
        create_button(text, row, col, lambda t=text: press(t), op_color)
    else:
        create_button(text, row, col, lambda t=text: press(t), btn_color)

create_button("Log", 5, 0, log_func, "#2563eb")
create_button("Pow(x,y)", 5, 1, power, "#2563eb")
create_button("Mod", 5, 2, mod, "#2563eb")
create_button("=", 5, 3, equal, equal_color)

root.mainloop()
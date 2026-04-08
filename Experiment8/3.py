import tkinter as tk
import math
import re
import webview
import threading

root = tk.Tk()
root.title("Smart Calculator")
root.geometry("480x620")
root.configure(bg="#0f172a")

expression = ""
equation = tk.StringVar()

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

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

def open_browser(url):
    """This function handles the pywebview window creation"""
    webview.create_window("Browser View", url, width=800, height=600)
    webview.start()

def equal():
    global expression
    expr = expression.strip()
    if not expr: return

    # 1. URL Detective Logic
    domain_pattern = re.compile(r'^[a-zA-Z0-9-]+\.[a-zA-Z]{2,}')
    is_url = False
    
    if expr.startswith(("http://", "https://", "www.")):
        is_url = True
    elif domain_pattern.match(expr) and not any(op in expr for op in ['+', '*', '(', ')', '=']):
        is_url = True

    # 2. Route the Input
    if is_url:
        if not expr.startswith(("http://", "https://")):
            expr = "https://" + expr
        
        equation.set("Opened in Browser")
        expression = ""
        
        # We MUST run pywebview in a separate thread, otherwise it freezes Tkinter
        browser_thread = threading.Thread(target=open_browser, args=(expr,), daemon=True)
        browser_thread.start()
        
    else:
        # 3. Standard Math Evaluation
        try:
            result = str(eval(expr))
            equation.set(result)
            expression = result
        except:
            equation.set("Error")
            expression = ""

# --- UI Setup ---

entry = tk.Entry(root,
                 textvariable=equation,
                 font=("Consolas", 22),
                 bg="#020617",
                 fg="#38bdf8",
                 bd=0,
                 insertwidth=2,
                 justify="right")
entry.pack(fill="x", ipady=12, padx=10, pady=8)

frame = tk.Frame(root, bg="#0f172a")
frame.pack(fill="both", expand=True, padx=10, pady=5)

for i in range(6):
    frame.rowconfigure(i, weight=1, uniform="row")
for j in range(4):
    frame.columnconfigure(j, weight=1, uniform="col")

btn_color = "#22acb0"
op_color = "#dbc324"
equal_color = "#a61fb3"

def create_button(text, row, col, cmd, bg):
    tk.Button(frame,
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
    ('0',4,0), ('.',4,1), (',',4,2), ('+',4,3)
]

# Note: Swapped 'C' for ',' in the grid to allow Pow(x,y) input.
# Put clear button on the top row to make room.
create_button("C", 0, 3, clear, "red")

for (text,row,col) in buttons:
    if text in ['+','-','*','/']:
        create_button(text, row, col, lambda t=text: press(t), op_color)
    else:
        create_button(text, row, col, lambda t=text: press(t), btn_color)

create_button("Log", 5, 0, log_func, "#2563eb")
create_button("Pow(x,y)", 5, 1, power, "#2563eb")
create_button("Mod", 5, 2, mod, "#2563eb")
create_button("=", 5, 3, equal, equal_color)

root.mainloop()
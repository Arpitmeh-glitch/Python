import tkinter as tk
root = tk.Tk()
root.title("Mera GUI mahan")
root.geometry("500x500")
root.configure(background="white")
label=tk.Label(root,text=
"    ()    \n"
"   ||     \n" \
"   ||      \n" \
"    00       \n", font=("Courier",15),bg="navy",fg="white")
label.pack(pady=20)
root.mainloop()
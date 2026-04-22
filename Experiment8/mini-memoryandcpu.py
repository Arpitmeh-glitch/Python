import tkinter as tk

class MiniCPU:
    def __init__(self, size=10):
        self.memory = [0] * size
        self.acc = [0, 0]   # Two accumulators

    def valid(self, addr):
        return 0 <= addr < len(self.memory)

    def valid_acc(self, acc_id):
        return 0 <= acc_id < len(self.acc)

    def reset(self):
        self.memory = [0] * len(self.memory)
        self.acc = [0] * len(self.acc)


class CPUGUI:
    def __init__(self, root):
        self.cpu = MiniCPU()
        self.root = root
        self.root.title("Mini CPU Simulator (Multi-ACC)")
        self.root.geometry("700x500")
        self.root.configure(bg="#1e1e1e")

        # ===== TOP FRAME =====
        top_frame = tk.Frame(root, bg="#1e1e1e")
        top_frame.pack(pady=10)

        self.acc_label = tk.Label(
            top_frame,
            text="ACC0: 0 | ACC1: 0",
            font=("Consolas", 20, "bold"),
            fg="#00ffcc",
            bg="#1e1e1e"
        )
        self.acc_label.pack()

        # ===== INPUT FRAME =====
        input_frame = tk.Frame(root, bg="#1e1e1e")
        input_frame.pack(pady=10)

        self.entry = tk.Entry(
            input_frame,
            width=40,
            font=("Consolas", 12),
            bg="#2d2d2d",
            fg="white",
            insertbackground="white"
        )
        self.entry.grid(row=0, column=0, padx=10)

        tk.Button(
            input_frame, text="Execute",
            command=self.execute,
            bg="#007acc", fg="white", width=10
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            input_frame, text="Reset",
            command=self.reset,
            bg="#cc3300", fg="white", width=10
        ).grid(row=0, column=2, padx=5)

        # ===== MAIN FRAME =====
        main_frame = tk.Frame(root, bg="#1e1e1e")
        main_frame.pack(fill="both", expand=True)

        # ===== CONSOLE =====
        console_frame = tk.Frame(main_frame, bg="#1e1e1e")
        console_frame.pack(side="left", fill="both", expand=True, padx=10)

        tk.Label(console_frame, text="Console",
                 bg="#1e1e1e", fg="white", font=("Arial", 12)).pack()

        self.output = tk.Text(
            console_frame,
            bg="#000000",
            fg="#00ff00",
            font=("Consolas", 10),
            height=15
        )
        self.output.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(self.output)
        scrollbar.pack(side="right", fill="y")
        self.output.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.output.yview)

        # ===== MEMORY =====
        memory_frame = tk.Frame(main_frame, bg="#1e1e1e")
        memory_frame.pack(side="right", padx=10)

        tk.Label(memory_frame, text="Memory",
                 bg="#1e1e1e", fg="white", font=("Arial", 12)).pack()

        self.memory_list = tk.Listbox(
            memory_frame,
            bg="#2d2d2d",
            fg="white",
            font=("Consolas", 10),
            width=25
        )
        self.memory_list.pack()

        self.update_memory_display()

    # ===== FUNCTIONS =====
    def log(self, msg):
        self.output.insert(tk.END, msg + "\n")
        self.output.see(tk.END)

    def update_memory_display(self):
        self.memory_list.delete(0, tk.END)
        for i, val in enumerate(self.cpu.memory):
            self.memory_list.insert(tk.END, f"[{i}] → {val}")

    def update_acc(self):
        text = " | ".join([f"ACC{i}: {val}" for i, val in enumerate(self.cpu.acc)])
        self.acc_label.config(text=text)

    def execute(self):
        command = self.entry.get().strip().split()
        self.entry.delete(0, tk.END)

        if not command:
            return

        cmd = command[0].upper()

        try:
            if cmd == "STORE":
                addr = int(command[1])
                value = int(command[2])

                if self.cpu.valid(addr):
                    self.cpu.memory[addr] = value
                    self.log(f"✔ Stored {value} at [{addr}]")
                else:
                    self.log("❌ Invalid memory address")

            elif cmd == "LOAD":
                acc_id = int(command[1])
                addr = int(command[2])

                if self.cpu.valid(addr) and self.cpu.valid_acc(acc_id):
                    self.cpu.acc[acc_id] = self.cpu.memory[addr]
                    self.log(f"✔ ACC{acc_id} loaded {self.cpu.acc[acc_id]}")
                else:
                    self.log("❌ Invalid ACC or memory address")

            elif cmd == "ADD":
                acc_id = int(command[1])
                addr = int(command[2])

                if self.cpu.valid(addr) and self.cpu.valid_acc(acc_id):
                    self.cpu.acc[acc_id] += self.cpu.memory[addr]
                    self.log(f"✔ ACC{acc_id} = {self.cpu.acc[acc_id]}")
                else:
                    self.log("❌ Invalid ACC or memory address")

            elif cmd == "SUB":
                acc_id = int(command[1])
                addr = int(command[2])

                if self.cpu.valid(addr) and self.cpu.valid_acc(acc_id):
                    self.cpu.acc[acc_id] -= self.cpu.memory[addr]
                    self.log(f"✔ ACC{acc_id} = {self.cpu.acc[acc_id]}")
                else:
                    self.log("❌ Invalid ACC or memory address")

            elif cmd == "SHOW":
                self.log(" | ".join([f"ACC{i}={val}" for i, val in enumerate(self.cpu.acc)]))

            else:
                self.log("❌ Invalid command")

        except:
            self.log("❌ Invalid format")

        self.update_acc()
        self.update_memory_display()

    def reset(self):
        self.cpu.reset()
        self.update_acc()
        self.update_memory_display()
        self.output.delete(1.0, tk.END)
        self.log("🔄 System Reset")


# ===== RUN APP =====
if __name__ == "__main__":
    root = tk.Tk()
    app = CPUGUI(root)
    root.mainloop()
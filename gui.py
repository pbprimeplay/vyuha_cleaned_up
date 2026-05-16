import tkinter as tk
from tkinter import ttk
import calculator

class ModernCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Nexus Calc Pro")
        self.root.geometry("350x450")
        self.root.configure(bg="#2d2d2d") # Sleek dark theme background
        
        # Configure styles for Themed Tkinter (ttk)
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure('TLabel', background='#2d2d2d', foreground='#ffffff', font=('Helvetica', 10))
        self.style.configure('TButton', font=('Helvetica', 10, 'bold'), padding=6)
        
        self.create_widgets()

    def create_widgets(self):
        # Main container frame with nice padding
        main_frame = ttk.Frame(self.root, padding="20 20 20 20")
        main_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Header Display
        header = tk.Label(main_frame, text="NEXUS CORE V2", bg="#2d2d2d", fg="#00ffcc", font=('Helvetica', 12, 'bold'))
        header.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Input Fields
        ttk.Label(main_frame, text="First Number:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.num1_entry = ttk.Entry(main_frame, width=15, font=('Helvetica', 11))
        self.num1_entry.grid(row=1, column=1, sticky=tk.E, pady=5)

        ttk.Label(main_frame, text="Second Number:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.num2_entry = ttk.Entry(main_frame, width=15, font=('Helvetica', 11))
        self.num2_entry.grid(row=2, column=1, sticky=tk.E, pady=5)

        # Dropdown Menu for Operations (Much better than an entry text box!)
        ttk.Label(main_frame, text="Operation:").grid(row=3, column=0, sticky=tk.W, pady=10)
        self.op_combobox = ttk.Combobox(main_frame, values=["add", "sub", "mult", "div", "pow"], state="readonly", width=13)
        self.op_combobox.grid(row=3, column=1, sticky=tk.E, pady=10)
        self.op_combobox.current(0)

        # Action Button
        self.calc_btn = tk.Button(main_frame, text="COMPUTE", bg="#00ffcc", fg="#2d2d2d", 
                                  font=('Helvetica', 11, 'bold'), activebackground="#00cc99", command=self.handle_calculation)
        self.calc_btn.grid(row=4, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E))

        # Beautiful Result Card
        self.result_card = tk.Frame(main_frame, bg="#1e1e1e", padx=10, pady=15, relief="groove", bd=1)
        self.result_card.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        self.result_title = tk.Label(self.result_card, text="ENGINE STATUS", bg="#1e1e1e", fg="#888888", font=('Helvetica', 8, 'bold'))
        self.result_title.pack(anchor=tk.W)
        
        self.result_text = tk.Label(self.result_card, text="Ready", bg="#1e1e1e", fg="#ffffff", font=('Helvetica', 14, 'bold'))
        self.result_text.pack(pady=(5, 0))

    def handle_calculation(self):
        op = self.op_combobox.get()
        n1 = self.num1_entry.get().strip()
        n2 = self.num2_entry.get().strip()
        
        try:
            res = calculator.calc(op, n1, n2)
            self.result_title.config(text="CALCULATION SUCCESSFUL", fg="#00ffcc")
            self.result_text.config(text=str(res), fg="#ffffff")
        except ValueError:
            self.result_title.config(text="INPUT ERROR", fg="#ff3333")
            self.result_text.config(text="Enter valid numbers", fg="#ff3333")
        except Exception as e:
            self.result_title.config(text="ENGINE CRASH", fg="#ff3333")
            self.result_text.config(text=str(e), fg="#ff3333")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernCalculatorGUI(root)
    root.mainloop()
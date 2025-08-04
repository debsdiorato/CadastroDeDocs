#arquivo principal
import tkinter as tk
from app.interface import AppInterface

if __name__ == "__main__":
    root = tk.Tk()
    app = AppInterface(root)
    root.mainloop()
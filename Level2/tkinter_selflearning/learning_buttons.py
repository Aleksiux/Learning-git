import tkinter as tk
import subprocess

parent_window = tk.Tk()
parent_window.geometry("550x550")


def func(cmd):
    subprocess.run(["powershell", cmd], shell=True)


button1 = tk.Button(parent_window, text='SPSS', height=4, width=10, command=lambda: func("pwd"))
button1.grid(row=1, column=0, pady=5, padx=5)
button2 = tk.Button(parent_window, text='Row2', height=4, width=10)
button2.grid(row=1, column=1, pady=5, padx=5)
button3 = tk.Button(parent_window, text='Row3', height=4, width=10)
button3.grid(row=1, column=2, pady=5, padx=5)
button4 = tk.Button(parent_window, text='Row4', height=4, width=10)
button4.grid(row=2, column=0, pady=5, padx=5)
button5 = tk.Button(parent_window, text='Row5', height=4, width=10)
button5.grid(row=2, column=1, pady=5, padx=5)
parent_window.mainloop()

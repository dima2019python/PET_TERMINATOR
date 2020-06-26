from tkinter import Button


class RootWindowSettings:
    def __init__(self, root, eat_func):
        btn = Button(root, text="кормить", background="#555", foreground="#ccc",
                     padx="20", pady="8", font="16", command=eat_func)
        btn.pack()

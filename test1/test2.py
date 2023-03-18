#!/usr/bin/python3
import tkinter as tk


class Test1App:
    def __init__(self, master=None):
        # build ui
        labelframe1 = tk.LabelFrame(master)
        labelframe1.configure(height=200, text='labelframe1', width=200)
        panedwindow2 = tk.PanedWindow(labelframe1, orient="horizontal")
        panedwindow2.configure(height=200, width=200)
        panedwindow2.pack(side="top")
        listbox2 = tk.Listbox(labelframe1)
        listbox2.pack(side="top")
        frame3 = tk.Frame(labelframe1)
        frame3.configure(height=200, width=200)
        label3 = tk.Label(frame3)
        label3.configure(
            cursor="arrow",
            justify="left",
            relief="flat",
            text='성동구')
        label3.grid(column=0, row=0)
        label4 = tk.Label(frame3)
        label4.configure(text='박윤아')
        label4.grid(column=1, row=0)
        frame3.pack(side="top")
        labelframe1.pack(side="top")

        # Main widget
        self.mainwindow = labelframe1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = Test1App(root)
    app.run()


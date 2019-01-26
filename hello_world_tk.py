# -*- encoding: utf-8 -*-
import tkinter as Tk


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Simple GUI")

        self.label = Tk.Label(master, text="Primera Ventana!")
        self.label.pack()

        self.great_button = Tk.Button(
            master,
            text="Hola Mundo!",
            command=self.great
        )
        self.great_button.pack()

        self.close_button = Tk.Button(
            master,
            text="Close",
            command=master.quit
        )
        self.close_button.pack()

    def great(self):
        print("Hello World!")

root = Tk.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

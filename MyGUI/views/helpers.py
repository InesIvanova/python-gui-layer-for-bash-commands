from tkinter import Tk


def destroy_view(func):
    def wrapper(tk: Tk):
        [slave.grid_forget() for slave in tk.grid_slaves()]
        [slave.pack_forget() for slave in tk.pack_slaves()]
        func(tk)
    return wrapper

from tkinter import Tk

from MyGUI.views.main import render_main


def setup_window():
    tk = Tk()
    tk.geometry("500x500")
    tk.title("Basic interface layer of bash commands")
    render_main(tk)
    return tk


def start(tk):
    tk.mainloop()


if __name__ == "__main__":
    window = setup_window()
    start(window)

from tkinter import Tk, Button

from MyGUI.views.vital_view import render_vital_functions


def render_main(tk: Tk) -> None:
    Button(tk, text="Vital", bg="green", fg="white", command=lambda: render_vital_functions(tk)).pack()

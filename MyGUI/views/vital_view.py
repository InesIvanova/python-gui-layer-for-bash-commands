from tkinter import Button, Tk

from MyGUI.controller.vital.commands import put_pc_to_sleep, logout_user, shutdown, cancel_shutdown
from MyGUI.views.helpers import destroy_view


@destroy_view
def render_vital_functions(tk: Tk) -> None:
    Button(tk, text="Logout", bg="green", fg="white", command=logout_user).pack()
    Button(tk, text="Suspend/hibernate computer", bg="orange", fg="white", command=put_pc_to_sleep).pack()
    Button(tk, text="Shut down computer", bg="red", fg="white", command=shutdown).pack()
    Button(tk, text="Cancel shutting down", bg="yellow", fg="black", command=cancel_shutdown).pack()

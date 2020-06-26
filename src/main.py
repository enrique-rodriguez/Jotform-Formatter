from tkinter import *
from tkinter.ttk import *

from config.constants import (
    APP_NAME,
    DIMENSIONS,
)

from app import Application

if __name__ == '__main__':
    """Entry Point"""

    root = Tk()
    root.title(APP_NAME)
    root.geometry(DIMENSIONS)

    style = Style()

    style.configure('W.TButton', font=(
        'calibri', 10, 'bold', 'underline'), foreground='#009420')

    app = Application(master=root)
    app.mainloop()

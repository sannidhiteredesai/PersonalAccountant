import tkinter as tk
from tkinter import ttk
from pa.ui.homeui import HomePage
from pa.ui.bankui import BankPage


LARGE_FONT = ('Verdana', 12)
NORMAL_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)


def setup(app):
    # Set window size same as screen size
    app.geometry(str(app.winfo_screenwidth()) + 'x' + str(app.winfo_screenheight()))

    # Open window always in maximized size
    app.state('zoomed')

    # Set window icon
    # app.iconbitmap(default='letter_p.ico')

    # Set window title
    app.title('Personal Accountant')

def start(app):
    setup(app)
    app.mainloop()


def popupmsg(msg):
    popup = tk.Tk()
    label = ttk.Label(popup, text=msg, font=NORMAL_FONT)
    label.pack(side='top', padx=10, pady=10)
    button = ttk.Button(popup, text='OK', command=popup.destroy)
    button.pack()
    popup.mainloop()


class PersonalAccountantApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self._setup_menubar(container)

        self.frames = {}

        for page in (HomePage, BankPage):
            frame = page(container, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def _setup_menubar(self, container):
        menubar = tk.Menu(container)

        # Menu tab
        home = tk.Menu(menubar, tearoff=0)
        home.add_command(label="Back to Home", command=lambda: self.show_frame(HomePage))
        home.add_separator()
        home.add_command(label="Exit", command=quit)
        menubar.add_cascade(label='Home', menu=home)

        # Menu tab
        bank = tk.Menu(menubar, tearoff=0)
        bank.add_command(label="View Banks", command=lambda: popupmsg('Not supported yet !'))
        bank.add_command(label="Add Bank", command=lambda: popupmsg('Not supported yet !'))
        menubar.add_cascade(label='Bank', menu=bank)

        tk.Tk.config(self, menu=menubar)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

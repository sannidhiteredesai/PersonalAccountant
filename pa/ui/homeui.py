import tkinter as tk
from tkinter import ttk
from pa.ui.bankui import BankPage

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        bank_button = ttk.Button(self, text='Banks',
                                 command=lambda: controller.show_frame(BankPage))
        bank_button.pack()

        fds_button = ttk.Button(self, text='FDs',
                                command=lambda: print('NYI'))
        fds_button.pack()

        savings_button = ttk.Button(self, text='Savings',
                                    command=lambda: print('NYI'))
        savings_button.pack()


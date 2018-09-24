import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Separator

bg_color = 'white'


class FDPage(tk.Frame):
    """
    Page displaying all bank details
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create a canvas object and a vertical scrollbar for scrolling it
        canvas = self._get_vertical_scrollable_canvas()

        # Create a frame inside the canvas which will be scrolled with it
        self.interior = tk.Frame(canvas)
        self.interior.configure(background=bg_color)
        interior_id = canvas.create_window(0, 0, window=self.interior, anchor=tk.NW)
        self._sync_frame_and_canvas_size(canvas,interior_id)

        self.banks = [
            {
                'bank_name': 'ABC Bank' + str(i),
                'bank_branch': 'ABC Branch',
                'bank_branch_code': 'ABC01',
                'bank_address': 'Address of bank zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz',
                'bank_timings': [],
                'bank_ifsc_code': 'IFSCCODE',
                'bank_micr_code': 'MICRCODE',
                'bank_phone_numbers': ['1111'],
                'bank_email': 'email',
                'bank_website': 'website',
            }
            for i in range(3)
        ]
        self._display_banks_header()
        self._display_each_bank_entry()

    def _sync_frame_and_canvas_size(self, canvas, interior_id):
        """
        Track changes to the canvas and frame width and sync them,
        also updating the scrollbar to match the size of the inner frame
        """

        def _configure_interior(event):
            size = (self.interior.winfo_reqwidth(), self.interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if self.interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=self.interior.winfo_reqwidth())

        def _configure_canvas(event):
            if self.interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        self.interior.bind('<Configure>', _configure_interior)
        canvas.bind('<Configure>', _configure_canvas)

    def _get_vertical_scrollable_canvas(self):
        vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0, yscrollcommand=vscrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        vscrollbar.config(command=canvas.yview)
        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
        return canvas

    def _display_banks_header(self):
        for col in range(11):
            # Expand each column when window is large
            self.interior.grid_columnconfigure(col, weight=1)

        # Set min size of address column
        self.interior.grid_columnconfigure(3, minsize=100)

        ttk.Label(self.interior, text='Bank Name', anchor='center',
                  borderwidth=2, relief="groove").grid(row=0, column=0, sticky='ew')
        ttk.Label(self.interior, text='Branch', anchor='center',
                  borderwidth=2, relief="groove").grid(row=0, column=1, sticky='ew')
        ttk.Label(self.interior, text='Branch Code', anchor='center',
                  borderwidth=2, relief="groove").grid(row=0, column=2, sticky='ew')
        ttk.Label(self.interior, text='Address', anchor='center',
                  borderwidth=2, relief="groove").grid(row=0, column=3, sticky='ew')
        ttk.Label(self.interior, text='Timings', anchor='center',
                  borderwidth=2, relief="groove").grid(row=0, column=4, sticky='ew')
        ttk.Label(self.interior, text='IFSC Code', anchor='center',
                  borderwidth=2, relief="groove").grid(row=0, column=5, sticky='ew')
        ttk.Label(self.interior, text='MICR Code', anchor='center',
                  borderwidth=2, relief="groove").grid(row=0, column=6, sticky='ew')
        ttk.Label(self.interior, text='Contact', anchor='center',
                  borderwidth=2, relief="groove").grid(row=0, column=7, sticky='ew')
        ttk.Label(self.interior, text='Email', anchor='center',
                  borderwidth=2, relief="groove").grid(row=0, column=8, sticky='ew')
        ttk.Label(self.interior, text='Website', anchor='center',
                  borderwidth=2, relief="groove").grid(row=0, column=9, sticky='ew')
        ttk.Label(self.interior, text='', anchor='center',
                  borderwidth=2, relief="groove").grid(row=0, column=10, sticky='ew')

    def _display_each_bank_entry(self):
        row = 1
        for bank in self.banks:
            fg_color = 'black' if (row + 1) % 4 == 0 else 'blue'

            ttk.Label(self.interior, text=bank['bank_name'], foreground=fg_color, background=bg_color,
                      anchor='center').grid(row=row, column=0, sticky='nsew', pady=(40, 40))
            ttk.Label(self.interior, text=bank['bank_branch'], foreground=fg_color, background=bg_color,
                      anchor='center').grid(row=row, column=1, sticky='ew', pady=(40, 40))
            ttk.Label(self.interior, text=bank['bank_branch_code'], foreground=fg_color, background=bg_color,
                      anchor='center').grid(row=row, column=2, sticky='ew', pady=(40, 40))
            ttk.Label(self.interior, text=bank['bank_address'], foreground=fg_color, background=bg_color,
                      anchor='center', wraplength=100).grid(row=row, column=3, sticky='ew')
            ttk.Label(self.interior, text=bank['bank_timings'], foreground=fg_color, background=bg_color,
                      anchor='center').grid(row=row, column=4, sticky='ew', pady=(40, 40))
            ttk.Label(self.interior, text=bank['bank_ifsc_code'], foreground=fg_color, background=bg_color,
                      anchor='center').grid(row=row, column=5, sticky='ew', pady=(40, 40))
            ttk.Label(self.interior, text=bank['bank_micr_code'], foreground=fg_color, background=bg_color,
                      anchor='center').grid(row=row, column=6, sticky='ew', pady=(40, 40))
            ttk.Label(self.interior, text=bank['bank_phone_numbers'], foreground=fg_color, background=bg_color,
                      anchor='center').grid(row=row, column=7, sticky='ew', pady=(40, 40))
            ttk.Label(self.interior, text=bank['bank_email'], foreground=fg_color, background=bg_color,
                      anchor='center').grid(row=row, column=8, sticky='ew', pady=(40, 40))
            ttk.Label(self.interior, text=bank['bank_website'], foreground=fg_color, background=bg_color,
                      anchor='center').grid(row=row, column=9, sticky='ew', pady=(40, 40))

            # Edit button
            button = ttk.Button(self.interior, text='Edit', cursor="hand2")
            button.grid(row=row, column=10)
            button.bind("<Button-1>", lambda e: print(e))

            # Line seperator
            sep = Separator(self.interior, orient="horizontal")
            sep.grid(row=row + 1, column=0, columnspan=11, sticky="ew")

            row += 2

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Separator
import os
from pa.bank import BankCollection


bg_color = 'white'
details_min_size = 300


class BankPage(tk.Frame):
    """
    Page displaying all bank details
    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.banks = BankCollection()
        banks = [
            {
                'bank_name': 'ABC Bank1',
                'bank_branch': 'ABC Branch1',
                'bank_branch_code': 'ABC01',
                'bank_address': 'Address of bank zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz zzzzzzzz',
                'bank_timings': [],
                'bank_ifsc_code': 'IFSCCODE',
                'bank_micr_code': 'MICRCODE',
                'bank_phone_numbers': ['1111'],
                'bank_email': 'email',
                'bank_website': 'website',
            },
            {
                'bank_name': 'ABC Bank2',
                'bank_branch': 'ABC Branch2',
                'bank_branch_code': 'ABC01',
                'bank_address': 'Address of bank zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz zzzzzzzz',
                'bank_timings': [],
                'bank_ifsc_code': 'IFSCCODE',
                'bank_micr_code': 'MICRCODE',
                'bank_phone_numbers': ['1111'],
                'bank_email': 'email',
                'bank_website': 'website',
            },
            {
                'bank_name': 'ABC Bank3',
                'bank_branch': 'ABC Branch3',
                'bank_branch_code': 'ABC01',
                'bank_address': 'Address of bank zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz zzzzzzzz',
                'bank_timings': [],
                'bank_ifsc_code': 'IFSCCODE',
                'bank_micr_code': 'MICRCODE',
                'bank_phone_numbers': ['1111'],
                'bank_email': 'email',
                'bank_website': 'website',
            },
            {
                'bank_name': 'ABC Bank4',
                'bank_branch': 'ABC Branch4',
                'bank_branch_code': 'ABC01',
                'bank_address': 'Address of bank zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz zzzzzzzz',
                'bank_timings': [],
                'bank_ifsc_code': 'IFSCCODE',
                'bank_micr_code': 'MICRCODE',
                'bank_phone_numbers': ['1111'],
                'bank_email': 'email',
                'bank_website': 'website',
            },
            {
                'bank_name': 'ABC Bank5',
                'bank_branch': 'ABC Branch5',
                'bank_branch_code': 'ABC01',
                'bank_address': 'Address of bank zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz zzzzzzzz',
                'bank_timings': [],
                'bank_ifsc_code': 'IFSCCODE',
                'bank_micr_code': 'MICRCODE',
                'bank_phone_numbers': ['1111'],
                'bank_email': 'email',
                'bank_website': 'website',
            },
        ]
        for bank in banks:
            self.banks.add(bank)

        self.controller = controller
        self._create_canvas_and_frame()
        self._cofigure_columns()
        self._display_contents()

    def _create_canvas_and_frame(self):
        """
        This method will create a canvas object with a vertical scrollbar for scrolling it
        and then a frame is created inside the canvas which will be scrolled with it
        """
        canvas = self._get_vertical_scrollable_canvas()
        self.interior = tk.Frame(canvas)
        self.interior.configure(background=bg_color)
        interior_id = canvas.create_window(0, 0, window=self.interior, anchor=tk.NW)
        self._sync_frame_and_canvas_size(canvas, interior_id)

    def _get_vertical_scrollable_canvas(self):
        """
        This method will return new canvas with vertical scrollbar inside it
        :return: canvas
        """
        vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0, yscrollcommand=vscrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        vscrollbar.config(command=canvas.yview)
        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
        return canvas

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

    def _cofigure_columns(self):
        """
        Set minimum size of address column and expand each column when window is large
        """
        self.interior.grid_columnconfigure(0, minsize=details_min_size)
        for col in range(5):
            self.interior.grid_columnconfigure(col, weight=1)

    def _display_contents(self):
        """
        This method will display contents of frame = bank header + bank details
        Every time this method is called, the frame will be refreshed to display all contents again
        """
        self._display_banks_header()
        self._display_each_bank_entry()

    def _display_banks_header(self):
        """
        This method will display bank header columns and an extra column header for edit button
        """
        label_options = {
            'anchor': 'center',
            'relief': 'groove',
            'borderwidth': 2,
            'font': ('Verdana', 11),
            'height': 2,
        }
        grid_options = {
            'sticky': 'ew',
            'pady': (10, 10),
        }
        tk.Label(self.interior, text='DETAILS', **label_options).grid(row=0, column=0, **grid_options)
        tk.Label(self.interior, text='TIMINGS', **label_options).grid(row=0, column=1, **grid_options)
        tk.Label(self.interior, text='CODES', **label_options).grid(row=0, column=2, **grid_options)
        tk.Label(self.interior, text='CONTACT', **label_options).grid(row=0, column=3, **grid_options)
        tk.Label(self.interior, text='EDIT', **label_options).grid(row=0, column=4, **grid_options)

    def _display_each_bank_entry(self):
        """
        This method will display bank details for each branch and an edit button for each row
        """
        row = 1
        self.img = tk.PhotoImage(file=os.path.join('pa', 'ui', 'images', 'edit.gif'))

        for bank in self.banks.get_all_bank_details():
            fg_color = 'black' if (row - 1) % 16 == 0 else 'blue'

            # Bank Details
            ttk.Label(self.interior, text='Name: ' + bank['bank_name'], foreground=fg_color, background=bg_color,
                      anchor='w').grid(row=row, column=0, sticky='ew', padx=(10, 0))
            ttk.Label(self.interior, text='Branch: ' + bank['bank_branch'], foreground=fg_color, background=bg_color,
                      anchor='w').grid(row=row + 1, column=0, sticky='ew', padx=(10, 0))
            ttk.Label(self.interior, text='Branch Code: ' + bank['bank_branch_code'], foreground=fg_color,
                      background=bg_color, anchor='w').grid(row=row + 2, column=0, sticky='ew', padx=(10, 0))
            ttk.Label(self.interior, text='Address: ' + bank['bank_address'], foreground=fg_color, background=bg_color,
                      anchor='w', wraplength=details_min_size).grid(row=row + 3, column=0, sticky='ew', rowspan=4,
                                                                    padx=(10, 0))

            # Bank Timings
            for i in range(7):
                ttk.Label(self.interior, text='MONDAY: 10:30 AM - 1:30 PM', foreground=fg_color, background=bg_color,
                          anchor='w').grid(row=row + i, column=1, sticky='ew', padx=(10, 0))

            # Bank Codes
            ttk.Label(self.interior, text='IFSC Code: ' + bank['bank_ifsc_code'], foreground=fg_color,
                      background=bg_color,
                      anchor='w').grid(row=row + 2, column=2, sticky='ew', padx=(10, 0))
            ttk.Label(self.interior, text='MICR Code: ' + bank['bank_micr_code'], foreground=fg_color,
                      background=bg_color,
                      anchor='w').grid(row=row + 3, column=2, sticky='ew', padx=(10, 0))

            # Bank Contact
            ttk.Label(self.interior, text='Telephone: ' + ','.join(bank['bank_phone_numbers']), foreground=fg_color,
                      background=bg_color, anchor='w').grid(row=row + 2, column=3, sticky='ew', padx=(10, 0))
            ttk.Label(self.interior, text='Email: ' + bank['bank_email'], foreground=fg_color, background=bg_color,
                      anchor='w').grid(row=row + 3, column=3, sticky='ew', padx=(10, 0))
            ttk.Label(self.interior, text='Website: ' + bank['bank_website'], foreground=fg_color, background=bg_color,
                      anchor='w').grid(row=row + 4, column=3, sticky='ew', padx=(10, 0))

            # Edit button

            button = tk.Button(self.interior, image=self.img, cursor="hand2", height=50, width=50,
                               command=lambda bank=bank: self._edit_bank(bank), text='Hi')
            button.grid(row=row, column=4, rowspan=6)

            # Line seperator
            sep = Separator(self.interior, orient="horizontal")
            sep.grid(row=row + 7, column=0, columnspan=11, sticky="ew", pady=(10, 10))

            row += 8

    def _edit_bank(self, bank):
        edit_bank_dialog = tk.Tk()
        label = ttk.Label(edit_bank_dialog, text=bank['bank_name'])
        label.pack(side='top', padx=10, pady=10)
        button = ttk.Button(edit_bank_dialog, text='OK',
                            command=lambda: self._close_and_refresh_page(edit_bank_dialog))
        button.pack()
        edit_bank_dialog.mainloop()

    def _close_and_refresh_page(self, widget_to_destroy):
        widget_to_destroy.destroy()
        self._display_contents()

import tkinter as tk
from tkinter import ttk, END, DISABLED
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

        self._screen_width = self.winfo_screenwidth()

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
                'bank_phone_numbers': ['1111', '22'],
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
        """
        This method will display a new window for editing bank details
        :param bank: <dict> containing that specific bank details
        """

        dialog = tk.Tk()
        self._setup_edit_bank_dialog(dialog)

        # Set columns to expand/shrink if window is resized
        for i in (0, 1, 10, 12, 13, 22):
            dialog.grid_columnconfigure(i, weight=1)

        # Add non-editable and editable details next to each other
        self.edited_name = self._add_entry_widget(parent=dialog, row=0, key='Bank:', value=bank['bank_name'])
        self.edited_branch = self._add_entry_widget(parent=dialog, row=1, key='Branch:', value=bank['bank_branch'])
        self.edited_address = self. _add_text_widget(parent=dialog, row=2, key='Address:', value=bank['bank_address'],
                                                     extra_options={'width': int(self._screen_width * 0.04), 'height': 10})
        self.edited_branch_code = self._add_entry_widget(parent=dialog, row=3, key='Branch Code:', value=bank['bank_branch_code'])
        # self.edited_timings = self._add_entry_widget(parent=dialog, row=4, key='Timings:', value=bank['bank_timings'])
        self._display_timings(dialog, row=4)
        self._display_timings(dialog, row=5)
        self._display_timings(dialog, row=6)
        self._display_timings(dialog, row=7)
        self._display_timings(dialog, row=8)
        self._display_timings(dialog, row=9)
        self._display_timings(dialog, row=10)

        self.edited_ifsc_code = self._add_entry_widget(parent=dialog, row=11, key='IFSC Code:', value=bank['bank_ifsc_code'])
        self.edited_micr_code = self._add_entry_widget(parent=dialog, row=12, key='MICR Code:', value=bank['bank_micr_code'])
        self.edited_phone_numbers = self._add_entry_widget(parent=dialog, row=13, key='Phone:', value=', '.join(bank['bank_phone_numbers']))
        self.edited_email = self._add_entry_widget(parent=dialog, row=14, key='Email:', value=bank['bank_email'])
        self.edited_website = self._add_entry_widget(parent=dialog, row=15, key='Website:', value=bank['bank_website'])
        self._add_vertical_seperator(dialog)

        self._add_bottom_buttons(dialog, bank=bank, row=16)
        dialog.mainloop()

    def _display_timings(self, dialog, row):
        tk.Label(dialog, text='Timings:', anchor='w').grid(row=row, column=0, sticky='ew', padx=(10, 10))
        tk.Label(dialog, text='Timings:', anchor='w').grid(row=row, column=12, sticky='ew', padx=(10, 10))

        ttk.Label(dialog, text='MONDAY').grid(row=row, column=1, sticky='e', padx=(0, 10))
        ttk.Label(dialog, text='MONDAY').grid(row=row, column=13, sticky='e', padx=(0, 10))

        e = tk.Entry(dialog, justify='center', width=3)
        e.insert('0', '10')
        e.grid(row=row, column=2)

        tk.Label(dialog, text=':').grid(row=row, column=3)

        e = tk.Entry(dialog, justify='center', width=3)
        e.insert('0', '30')
        e.grid(row=row, column=4)

        tk.Label(dialog, text='AM').grid(row=row, column=5)

        tk.Label(dialog, text='-').grid(row=row, column=6)

        e = tk.Entry(dialog, justify='center', width=3)
        e.insert('0', '11')
        e.grid(row=row, column=7)

        tk.Label(dialog, text=':').grid(row=row, column=8)

        e = tk.Entry(dialog, justify='center', width=3)
        e.insert('0', '30')
        e.grid(row=row, column=9)

        tk.Label(dialog, text='AM').grid(row=row, column=10, sticky='w', padx=(0, 10))

        # Non editable part


        e = tk.Entry(dialog, justify='center', width=3)
        e.insert('0', '10')
        e.grid(row=row, column=14)

        tk.Label(dialog, text=':').grid(row=row, column=15)

        e = tk.Entry(dialog, justify='center', width=3)
        e.insert('0', '30')
        e.grid(row=row, column=16)

        tk.Label(dialog, text='AM').grid(row=row, column=17)

        tk.Label(dialog, text='-').grid(row=row, column=18)

        e = tk.Entry(dialog, justify='center', width=3)
        e.insert('0', '11')
        e.grid(row=row, column=19)

        tk.Label(dialog, text=':').grid(row=row, column=20)

        e = tk.Entry(dialog, justify='center', width=3)
        e.insert('0', '30')
        e.grid(row=row, column=21)

        tk.Label(dialog, text='AM').grid(row=row, column=22, sticky='w', padx=(0, 10))


    def _add_vertical_seperator(self, dialog):
        # Line seperator
        sep = Separator(dialog, orient="vertical")
        sep.grid(row=0, column=11, rowspan=10, sticky="ns")

    def _add_text_widget(self, parent, row, key, value, extra_options={}):
        # Existing details
        ttk.Label(parent, text=key).grid(row=row, column=0, sticky='ew', padx=(10, 10), pady=(10, 0))
        existing_text = tk.Text(parent, relief='sunken', background='#%02x%02x%02x' % (240, 240, 237), **extra_options)
        existing_text.insert(END, value)
        existing_text.config(state=DISABLED)
        existing_text.grid(row=row, column=1, columnspan=10, sticky='ew', padx=(10, 10), pady=(10, 0))

        # Editable details
        ttk.Label(parent, text=key).grid(row=row, column=12, sticky='ew', padx=(10, 10), pady=(10, 0))
        editable_text = tk.Text(parent, **extra_options)
        editable_text.insert(END, value)
        editable_text.grid(row=row, column=13, columnspan=10, sticky='ew', padx=(10, 10), pady=(10, 0))

        return editable_text

    def _add_entry_widget(self, parent, row, key, value, extra_options={}):
        # Existing details
        ttk.Label(parent, text=key).grid(row=row, column=0, sticky='ew', padx=(10, 10), pady=(10, 0))
        existing_entry = tk.Entry(parent, relief='sunken', background='#%02x%02x%02x' % (240, 240, 237),
                                  disabledforeground='black', **extra_options)
        existing_entry.insert(END, value)
        existing_entry.config(state=DISABLED)
        existing_entry.grid(row=row, column=1, columnspan=10, sticky='ew', padx=(10, 10), pady=(10, 0))

        # Editable details
        ttk.Label(parent, text=key).grid(row=row, column=12, sticky='ew', padx=(10, 10), pady=(10, 0))
        editable_entry = tk.Entry(parent, **extra_options)
        editable_entry.insert(END, value)
        editable_entry.grid(row=row, column=13, columnspan=10, sticky='ew', padx=(10, 10), pady=(10, 0))

        return editable_entry

    def _close_and_refresh_page(self, widget_to_destroy):
        widget_to_destroy.destroy()
        self._display_contents()

    def _setup_edit_bank_dialog(self, dialog):
        """
        This method will:
            Set the dimensions of dialog box,
            Set its position to centre of screen,
            Set focus to the dialog box,
        :param dialog: Tkinter window for edit bank dialog
        """
        dailog_width = int(self.winfo_screenwidth()*0.85)
        dailog_height = int(self.winfo_screenheight()*0.8)
        dialog_x_cord = int((self.winfo_screenwidth() - dailog_width) / 2)
        dialog_y_cord = int((self.winfo_screenheight() - dailog_height) / 2) - 10
        dialog.geometry(f'{dailog_width}x{dailog_height}+{dialog_x_cord}+{dialog_y_cord}')
        dialog.focus_force()

    def _add_bottom_buttons(self, dialog, bank, row):

        delete = ttk.Button(dialog, text='Delete Existing Branch', command=lambda: self._show_confirm_dialog(dialog, bank))
        delete.grid(row=row, column=0, padx=(10, 10), pady=(10, 10), columnspan=11)

        save = ttk.Button(dialog, text='Save Updated Branch', command=lambda: self._show_confirm_dialog(dialog, bank))
        save.grid(row=row, column=12, padx=(10, 10), pady=(10, 10), columnspan=11)

    def _show_confirm_dialog(self, dialog, bank):
        confirm = tk.Tk()

        message = ttk.Label(confirm, text='Do you really want to save updated branch ?')
        message.grid(row=0, columnspan=2)

        yes = ttk.Button(confirm, text='Yes', command=lambda: self._save_branch(bank, dialog, confirm))
        yes.grid(row=1, column=0)

        no = ttk.Button(confirm, text='No', command=lambda: confirm.destroy())
        no.grid(row=1, column=1)

    def _save_branch(self, bank, edit_branch_dialog, confirm_dialog):
        confirm_dialog.destroy()
        updated_bank = {
            'bank_name': self.edited_name.get(),
            'bank_branch': self.edited_branch.get(),
            'bank_branch_code': self.edited_branch_code.get(),
            'bank_address': self.edited_address.get('0.0', END),
            'bank_timings': [],
            'bank_ifsc_code': self.edited_ifsc_code.get(),
            'bank_micr_code': self.edited_micr_code.get(),
            'bank_phone_numbers': [ _ for _ in map(str.strip, self.edited_phone_numbers.get().split(','))],
            'bank_email': self.edited_email.get(),
            'bank_website': self.edited_website.get(),
        }
        self.banks.update(updated_bank)
        self._close_and_refresh_page(edit_branch_dialog)
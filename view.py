from tkinter import Entry, Button, StringVar, Tk

class CalculatorView:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.entry_var = StringVar()
        self.entry = Entry(self.root, textvariable=self.entry_var)
        self.entry.grid(row=0, column=0, columnspan=4)
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
        ]
        row_val = 1
        col_val = 0
        for button in buttons:
            Button(self.root, text=button, command=lambda button=button: self.controller.button_click(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def set_controller(self, controller):
        self.controller = controller

    def set_entry_text(self, text):
        self.entry_var.set(text)

    def get_entry_text(self):
        return self.entry_var.get()

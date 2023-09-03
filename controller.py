class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.first_num = ""
        self.second_num = ""
        self.operator = ""

    def button_click(self, button):
        if button in ['+', '-', '*', '/']:
            self.operator = button
            self.first_num = self.view.get_entry_text()
            self.view.set_entry_text("")
        elif button == "=":
            self.second_num = self.view.get_entry_text()
            if self.operator == "+":
                result = self.model.add(float(self.first_num), float(self.second_num))
            elif self.operator == "-":
                result = self.model.subtract(float(self.first_num), float(self.second_num))
            elif self.operator == "*":
                result = self.model.multiply(float(self.first_num), float(self.second_num))
            elif self.operator == "/":
                result = self.model.divide(float(self.first_num), float(self.second_num))
            self.view.set_entry_text(str(result))
            self.first_num = ""
            self.second_num = ""
            self.operator = ""
        else:
            self.view.set_entry_text(self.view.get_entry_text() + button)

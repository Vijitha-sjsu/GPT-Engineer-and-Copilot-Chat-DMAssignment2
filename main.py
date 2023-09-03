from tkinter import Tk
from model import CalculatorModel
from view import CalculatorView
from controller import CalculatorController

def main():
    root = Tk()
    model = CalculatorModel()
    view = CalculatorView(root)
    controller = CalculatorController(model, view)
    view.set_controller(controller)
    root.mainloop()

if __name__ == "__main__":
    main()

from logic import Logic
from tkinter import Tk
from gui import Gui


def main() -> None:
    """Sets up and initializes the window from Tkinter, the logic behind it, and executes the main function"""
    window = Tk()
    window.title('Voting Form Application')
    window.geometry('300x350')
    window.resizable(False, False)
    gui = Gui(window)
    logic = Logic(gui)
    gui.set_logic(logic)
    window.mainloop()


if __name__ == '__main__':
    main()

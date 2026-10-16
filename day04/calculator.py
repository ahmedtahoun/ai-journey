from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x420+0+0")
        master.config(bg="gray")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ""

        # 1. Changed to .place() to match the buttons
        # 2. Added a solid border (relief='solid', bd=2) so it's visible on macOS
        # 3. Placed at y=10 so it doesn't hide under the title bar
        Entry(width=17, bg="red", fg="white", font=('Arial Bold', 28), textvariable=self.equation, relief='solid', bd=2).place(x=0, y=10)

        # Row 1 - Fixed the x coordinates to match the other rows (0, 90, 180, 270)
        Button(width=6, height=4, text='1', relief='flat', bg='white', command=lambda: self.show(1)).place(x=0, y=100)
        Button(width=6, height=4, text='2', relief='flat', bg='white', command=lambda: self.show(2)).place(x=90, y=100)
        Button(width=6, height=4, text='3', relief='flat', bg='white', command=lambda: self.show(3)).place(x=180, y=100)
        Button(width=6, height=4, text='+', relief='flat', bg='white', command=lambda: self.show('+')).place(x=270, y=100)

        # Row 2
        Button(width=6, height=4, text='4', relief='flat', bg='white', command=lambda: self.show(4)).place(x=0, y=180)
        Button(width=6, height=4, text='5', relief='flat', bg='white', command=lambda: self.show(5)).place(x=90, y=180)
        Button(width=6, height=4, text='6', relief='flat', bg='white', command=lambda: self.show(6)).place(x=180, y=180)
        Button(width=6, height=4, text='-', relief='flat', bg='white', command=lambda: self.show('-')).place(x=270, y=180)

        # Row 3
        Button(width=6, height=4, text='7', relief='flat', bg='white', command=lambda: self.show(7)).place(x=0, y=260)
        Button(width=6, height=4, text='8', relief='flat', bg='white', command=lambda: self.show(8)).place(x=90, y=260)
        Button(width=6, height=4, text='9', relief='flat', bg='white', command=lambda: self.show(9)).place(x=180, y=260)
        Button(width=6, height=4, text='*', relief='flat', bg='white', command=lambda: self.show('*')).place(x=270, y=260)

        # Row 4
        Button(width=6, height=4, text='C', relief='flat', bg='white', command=self.clear).place(x=0, y=340)
        Button(width=6, height=4, text='0', relief='flat', bg='white', command=lambda: self.show(0)).place(x=90, y=340)
        Button(width=6, height=4, text='=', relief='flat', bg='white', command=self.solve).place(x=180, y=340)
        Button(width=6, height=4, text='/', relief='flat', bg='white', command=lambda: self.show('/')).place(x=270, y=340)

    def show(self, value):
        print(f"Clicked: {value}")
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except Exception:
            self.equation.set("Error")
            self.entry_value = ""

root = Tk()
calculator = Calculator(root)
root.mainloop()
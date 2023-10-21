"""
__main__.py
"""

import tkinter as tk
from tkinter import ttk
import platform
import math


class App(tk.Tk):
    """
    App
    """

    def __init__(self) -> None:
        """
        Initialises app
        :return: None
        :rtype: None
        """

        super().__init__()

        self.resizable(False, False)
        self.title("Quadratic Solver")

        answer = tk.StringVar()
        answer.set("Waiting...")
        self.answer_label = ttk.Label(textvariable=answer)

        try:
            import sv_ttk
            sv_ttk.set_theme("dark")
        except:
            print("Theme Failed To Load, Reverting to native.")

            style = ttk.Style(self)

            if platform.system() == "Windows":
                style.theme_use("winnative")
            elif platform.system() == "Darwin":
                style.theme_use("aqua")
            else:
                style.theme_use("alt")

        self.copy_btn = ttk.Button(master=self, text="Copy", command=lambda: self.copy(answer.get().replace("\n", "")), state="disabled")

        a = tk.IntVar()
        b = tk.IntVar()
        c = tk.IntVar()

        grid_items = [
            [ttk.Label(master=self, text="Enter A:"), ttk.Entry(master=self, textvariable=a)],
            [ttk.Label(master=self, text="Enter B:"), ttk.Entry(master=self, textvariable=b)],
            [ttk.Label(master=self, text="Enter C:"), ttk.Entry(master=self, textvariable=c)],
            [self.answer_label, ttk.Button(master=self, text="Submit", command=lambda: answer.set(self.solve_quadratic(a, b, c)))],
            [None,  self.copy_btn]
        ]

        self.columnconfigure(0, weight=0, minsize=150)
        self.columnconfigure(1, weight=1, minsize=225)

        for i in range(len(grid_items)):
            self.rowconfigure(i, weight=1, minsize=50)

            for j in range(len(grid_items[i])):
                if grid_items[i][j] is None:
                    continue
                grid_items[i][j].grid(row=i, column=j, padx=10, pady=5)

    def solve_quadratic(self, a: tk.IntVar, b: tk.IntVar, c: tk.IntVar) -> str:
        """
        Solves the quadratic based on the parameters passed
        :param tk.IntVar a: Value in front of x^2
        :param tk.IntVar b: Value in front of x
        :param tk.IntVar c: Value without x or x^2
        :return: Answer formatted as 'x = {positive_answer} or x = {negative_answer}' | Error Message
        :rtype: str
        """

        # If a = 0 the equation does not work
        if a.get() == 0:
            self.answer_label.config(foreground="red")
            return "A cannot be 0!"

        try:
            # Calculates both answers
            positive_answer = (-b.get() + math.sqrt((b.get() ** 2) - (4 * a.get() * c.get()))) / (2 * a.get())
            negative_answer = (-b.get() - math.sqrt((b.get() ** 2) - (4 * a.get() * c.get()))) / (2 * a.get())

            self.answer_label.config(foreground="")
            self.copy_btn["state"] = "normal"
            return "x = " + str(positive_answer) + " \nor\n x = " + str(negative_answer)
        except:
            self.answer_label.config(foreground="red")
            self.copy_btn["state"] = "disabled"

            return "An error occurred! \nCheck your values."

    def copy(self, value: str) -> None:
        """
        Add an item to the user's clipboard

        :param str value: Value to copy to clipboard
        :return: None
        :rtype: None
        """

        self.clipboard_clear()
        self.clipboard_append(value)


if __name__ == "__main__":
    root = App()
    root.mainloop()

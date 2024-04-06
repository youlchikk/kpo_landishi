import functools

import customtkinter
import functions

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Calculator")
        self.geometry(f"{350}x{600}")

        self.grid_columnconfigure(4, weight=0)

        self.rowconfigure(6, weight=0)

        self.button_c = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#7D7D7D", text_color=("black"), text="C", command=functools.partial(functions.deleted, self))
        self.button_c.grid(row=1, column=0, padx=0, pady=0)
        self.button_plus_minus = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#7D7D7D", text_color=("black"), text="+/-", command=functools.partial(functions.button_neg, self))
        self.button_plus_minus.grid(row=1, column=1, padx=0, pady=0)
        self.button_percent = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#7D7D7D", border_width=2, border_color="black", text_color=("black"), text="%", command=functools.partial(functions.percent, self))
        self.button_percent.grid(row=1, column=2, padx=0, pady=0)
        self.button_division = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#DF7926", border_width=2, border_color="black", text_color=("white"), text="÷", command=functools.partial(functions.divide, self))
        self.button_division.grid(row=1, column=3, padx=0, pady=0)
        self.button_mult = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#DF7926", border_width=2, border_color="black", text_color=("white"), text="x", command=functools.partial(functions.mult, self))
        self.button_mult.grid(row=2, column=3, padx=0, pady=0)
        self.button_minus = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#DF7926", border_width=2, border_color="black", text_color=("white"), text="-", command=functools.partial(functions.minus, self))
        self.button_minus.grid(row=3, column=3, padx=0, pady=0)
        self.button_plus = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#DF7926", border_width=2, border_color="black", text_color=("white"), text="+", command=functools.partial(functions.addition, self))
        self.button_plus.grid(row=4, column=3, padx=0, pady=0)
        self.button_equal = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#DF7926", border_width=2, border_color="black", text_color=("white"), text="=", command=functools.partial(functions.equal, self))
        self.button_equal.grid(row=5, column=3, padx=0, pady=0)
        self.button_seven = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#272320", border_width=2, border_color="black", text_color=("white"), text="7", command=lambda: functions.button_click(self, 7))
        self.button_seven.grid(row=2, column=0, padx=0, pady=0)
        self.button_eight = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#272320", border_width=2, border_color="black", text_color=("white"), text="8", command=lambda: functions.button_click(self, 8))
        self.button_eight.grid(row=2, column=1, padx=0, pady=0)
        self.button_nine = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#272320", border_width=2, border_color="black", text_color=("white"), text="9", command=lambda: functions.button_click(self, 9))
        self.button_nine.grid(row=2, column=2, padx=0, pady=0)
        self.button_four = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#272320", border_width=2, border_color="black", text_color=("white"), text="4", command=lambda: functions.button_click(self, 4))
        self.button_four.grid(row=3, column=0, padx=0, pady=0)
        self.button_five = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#272320", border_width=2, border_color="black", text_color=("white"), text="5", command=lambda: functions.button_click(self, 5))
        self.button_five.grid(row=3, column=1, padx=0, pady=0)
        self.button_six = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#272320", border_width=2, border_color="black", text_color=("white"), text="6", command=lambda: functions.button_click(self, 6))
        self.button_six.grid(row=3, column=2, padx=0, pady=0)
        self.button_one = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#272320", border_width=2, border_color="black", text_color=("white"), text="1", command=lambda: functions.button_click(self,1))
        self.button_one.grid(row=4, column=0, padx=0, pady=0)
        self.button_two = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#272320", border_width=2, border_color="black", text_color=("white"), text="2", command=lambda: functions.button_click(self, 2))
        self.button_two.grid(row=4, column=1, padx=0, pady=0)
        self.button_three = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#272320", border_width=2, border_color="black", text_color=("white"), text="3", command=lambda: functions.button_click(self, 3))
        self.button_three.grid(row=4, column=2, padx=0, pady=0)
        self.button_zero = customtkinter.CTkButton(master=self, width=160, height=80, fg_color="#272320", border_width=2, border_color="black", text_color=("white"), text="0", command=lambda: functions.button_click(self, 0))
        self.button_zero.grid(row=5, column=0, columnspan=2,padx=0, pady=0)
        self.button_comma = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#272320", border_width=2, border_color="black", text_color=("white"), text=".", command=lambda: functions.button_click(self, '.'))
        self.button_comma.grid(row=5, column=2, padx=0, pady=0)
        self.textbox = customtkinter.CTkTextbox(self, width=350)
        self.textbox.grid(row=0, column=0, columnspan=4, padx=0, pady=0, sticky="nsew")

        self.f_num = 0
        self.math = ""

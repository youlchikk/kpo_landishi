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

        buttons_data = [
            [["C", functools.partial(functions.deleted, self)], ["+/-", functools.partial(functions.button_neg, self)], ["%", functools.partial(functions.percent, self)], ["÷", functools.partial(functions.divide, self)]],
            [["7", functools.partial(functions.button_click, self, 7)], ["8", functools.partial(functions.button_click, self, 8)], ["9", functools.partial(functions.button_click, self, 9)], ["x", functools.partial(functions.mult, self)]],
            [["4", functools.partial(functions.button_click, self, 8)], ["5", functools.partial(functions.button_click, self, 5)], ["6", functools.partial(functions.button_click, self, 6)], ["-", functools.partial(functions.minus, self)]],
            [["1", functools.partial(functions.button_click, self, 1)], ["2", functools.partial(functions.button_click, self, 2)], ["3", functools.partial(functions.button_click, self, 3)], ["+", functools.partial(functions.addition, self)]],
            [["0", functools.partial(functions.button_click, self, 0)], [".", functools.partial(functions.button_click, self, '.')], ["=", functools.partial(functions.equal, self)]]
        ]

        for row_text_button in range(len(buttons_data)):
            for ind_text_button in range(len(buttons_data[row_text_button])):
                button = customtkinter.CTkButton(master=self, width=80, height=80, fg_color="#7D7D7D", text_color=("black"), text=buttons_data[row_text_button][ind_text_button][0], command=buttons_data[row_text_button][ind_text_button][1])
                button.grid(row=row_text_button + 1, column=ind_text_button, padx=0, pady=0)

        self.textbox = customtkinter.CTkTextbox(self, width=350)
        self.textbox.grid(row=0, column=0, columnspan=4, padx=0, pady=0, sticky="nsew")

        self.f_num = 0
        self.math = ""

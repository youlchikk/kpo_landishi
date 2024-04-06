from decimal import Decimal


def button_click(self, number):
    current = self.textbox.get("0.0", "end").rstrip('\n')
    self.textbox.delete("0.0", "end")
    self.textbox.insert("0.0", str(current) + str(number))


def divide(self):
    first_number = self.textbox.get("0.0", "end")
    self.math = "divide"
    self.f_num = Decimal(first_number)
    self.textbox.delete("0.0", "end")


def addition(self):
    first_number = self.textbox.get("0.0", "end")
    self.math = "addition"
    self.f_num = Decimal(first_number)
    self.textbox.delete("0.0", "end")


def minus(self):
    first_number = self.textbox.get("0.0", "end")
    self.math = "minus"
    self.f_num = Decimal(first_number)
    self.textbox.delete("0.0", "end")


def mult(self):
    first_number = self.textbox.get("0.0", "end")
    self.math = "mult"
    self.f_num = Decimal(first_number)
    self.textbox.delete("0.0", "end")


def percent(self):
    first_number = self.textbox.get("0.0", "end")
    self.math = "percent"
    self.f_num = Decimal(first_number)
    self.textbox.delete("0.0", "end")


def equal(self):
    second_number = self.textbox.get("0.0", "end")
    self.textbox.delete("0.0", "end")

    if self.math == "addition":
        self.textbox.insert("0.0", self.f_num + Decimal(second_number))
    if self.math == "divide":
        self.textbox.insert("0.0", self.f_num / Decimal(second_number))
    if self.math == "minus":
        self.textbox.insert("0.0", self.f_num - Decimal(second_number))
    if self.math == "mult":
        self.textbox.insert("0.0", self.f_num * Decimal(second_number))
    if self.math == "percent":
        self.textbox.insert("0.0", self.f_num % Decimal(second_number))


def button_neg(self):
    current = self.textbox.get("0.0", "end")
    if current.startswith("-"):
        current = current[1:]
    else:
        current = "-" + current
    self.textbox.delete("0.0", "end")
    self.textbox.insert("0.0", current)


def deleted(self):
    self.textbox.delete("0.0", "end")


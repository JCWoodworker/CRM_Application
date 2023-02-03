import tkinter as tk

class Checkbox:
  def __init__(self, frame, text, bg, fg, row, column, padx=None, pady=None, variable=any):
    self.frame = frame
    self.text = text
    self.bg = bg
    self.fg = fg
    self.row = row
    self.column = column
    self.padx = padx
    self.pady = pady
    self.variable = variable

    self.checkbutton = tk.Checkbutton(self.frame, text=self.text, bg=self.bg, fg=self.fg, font=("Arial", 15), variable=self.variable)
    self.checkbutton.grid(row=self.row, column=self.column, padx=self.padx, pady=self.pady, sticky="ns")
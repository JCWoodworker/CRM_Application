import tkinter as tk

class Label:
  def __init__(self, frame, text, bg, fg, row, column, padx, pady, sticky):
    self.frame = frame
    self.text = text
    self.bg = bg
    self.fg = fg
    self.row = row
    self.column = column
    self.padx = padx
    self.pady = pady
    self.sticky = sticky

    self.label = tk.Label(self.frame, text=self.text, bg=self.bg, fg=self.fg, font=("Arial Bold", 22))
    self.label.grid(row=self.row, column=self.column, padx=self.padx, pady=self.pady, sticky=self.sticky)
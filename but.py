import tkinter as tk

class Button:
  def __init__(self, frame, text, bg, fg, row=None, column=None, padx=None, pady=None, width=None, height=None, command=None):
    self.frame = frame
    self.text = text
    self.bg = bg
    self.fg = fg
    self.row = row
    self.column = column
    self.padx = padx
    self.pady = pady
    self.width = width
    self.height = height
    self.command = command

    self.button = tk.Button(self.frame, text=self.text, bg=self.bg, fg=self.fg, font=("Arial", 15), height=self.height, width=10, command=self.command)
    self.button.grid(row=self.row, column=self.column, padx=self.padx, pady=self.pady, sticky="nswe")
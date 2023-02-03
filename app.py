import tkinter as tk
from class_button import Button
from class_label import Label


class App(tk.Tk):
  def __init__(self):
    super().__init__()
    #######################################
    #### ROOT/FRAME SETUPS AND CONFIGS ####
    #######################################

    self.root = tk.Tk()
    self.root.title("GUI Application Framework")
    self.root.configure(bg="white")

    # ***** ROOT GEOMETRY - SIZED AT 85% OF USER'S SCREEN *****

    self.screen_width = self.root.winfo_screenwidth()
    self.screen_height = self.root.winfo_screenheight()
    self.window_width = int(self.screen_width * 0.85)
    self.window_height = int(self.screen_height * 0.85)
    self.root.geometry(f"{self.window_width}x{self.window_height}")
    self.root.resizable(True, True)

    # ***** ROOT GRID CONFIGS *****

    self.root.columnconfigure(0, weight=1)
    self.root.columnconfigure(1, weight=4)
    self.root.rowconfigure(0, weight=1)
    self.root.rowconfigure(1, weight=10)
    self.root.rowconfigure(2, weight=2)

    # ***** FRAMES *****

    self.main_upper_frame = tk.Frame(self.root, bg="red", bd="10", relief="groove")
    self.main_middle_left_frame = tk.Frame(
        self.root, bg="purple", bd="10", relief="groove"
    )
    self.main_middle_right_frame = tk.Frame(
        self.root, bg="orange", bd="10", relief="groove"
    )
    self.main_lower_frame = tk.Frame(
        self.root, bg="green", bd="10", relief="groove"
    )

    self.main_upper_frame.grid(column=0, row=0, columnspan=2, sticky="nsew")
    self.main_middle_left_frame.grid(column=0, row=1, sticky="nsew")
    self.main_middle_right_frame.grid(column=1, row=1, sticky="nsew")
    self.main_lower_frame.grid(column=0, row=2, columnspan=2, sticky="nsew")

    # ***** FRAME GRID CONFIGS *****

    self.main_middle_left_frame.columnconfigure(0, weight=10)
    self.main_middle_left_frame.columnconfigure(1, weight=1)
    self.main_middle_left_frame.rowconfigure(0, weight=1)
    self.main_middle_left_frame.rowconfigure(1, weight=10)

    self.main_lower_frame.columnconfigure(0, weight=1)
    self.main_lower_frame.columnconfigure(1, weight=1)
    self.main_lower_frame.columnconfigure(2, weight=1)
    self.main_lower_frame.columnconfigure(3, weight=1)
    self.main_lower_frame.columnconfigure(4, weight=1)
    self.main_lower_frame.rowconfigure(0, weight=1)

    #################
    #### WIDGETS ####
    #################

    # #### FRAME LABELS ####

    self.label1 = Label(self.main_upper_frame, "Title Bar", "red", "black", 0, 0, 0, 0, "ew")
    self.label2 = Label(self.main_middle_right_frame, "Customer Information", "orange", "black", 0, 0, 0, 0, "ew")
    self.label3 = Label(self.main_middle_left_frame, "Customer List", "purple", "black", 0, 0, 0, 0, "ew")
    self.label4 = Label(self.main_lower_frame, "Footer Bar", "green", "black", 0, 0, 0, 0, "ew")

    #### LISTBOX WITH SCROLLBAR ####

    self.listbox = tk.Listbox(self.main_middle_left_frame, selectmode="single", bd=5, selectbackground="white", selectforeground="black")
    self.scrollbar = tk.Scrollbar(self.main_middle_left_frame, orient="vertical", command=self.listbox.yview)
    self.listbox.configure(yscrollcommand=self.scrollbar.set, font=("Arial", 18))

    self.listbox.grid(row=1, column=0, sticky="nsew")
    self.scrollbar.grid(row=1, column=1, sticky="ns")

    #### Sample Customer List ####

    for i in range(50):
      self.listbox.insert("end", f"Customer {i}")

app = App()
app.mainloop()

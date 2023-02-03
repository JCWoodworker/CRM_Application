import tkinter as tk
from class_button import Button
from class_label import Label
from class_checkbox import Checkbox


class App(tk.Tk):
    def __init__(self):
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

        #####################################
        # ***** VARIABLE DECLARATIONS ***** #
        #####################################

        self.checkbox1_variable = tk.IntVar()
        self.checkbox2_variable = tk.IntVar()
        self.checkbox3_variable = tk.IntVar()

        #########################
        #### *** WIDGETS *** ####
        #########################

        # ***** FRAME LABELS *****

        self.label1 = Label(
            self.main_upper_frame,
            "Top Bar - personal settings, color theme options, set username, ...",
            "red",
            "black",
            0,
            0,
            0,
            0,
            "ew",
        )
        self.label1 = Label(
            self.main_middle_right_frame,
            "Form Inputs - fields, checkboxes, submit button, etc ...",
            "orange",
            "black",
            0,
            0,
            0,
            0,
            "ew",
        )
        self.label3 = Label(
            self.main_middle_left_frame,
            "Searchable Operations:",
            "purple",
            "black",
            0,
            0,
            0,
            0,
            "ew",
        )

        # ***** LOWER FRAME BUTTONS *****

        self.cid_label = Label(
            self.main_lower_frame, "CID:", "green", "black", 0, 0, 0, 0, "w"
        )
        self.cid_entry = tk.Entry(self.main_lower_frame, font=("Arial", 18))

        self.button1 = Button(
            self.main_lower_frame, "Quick Operation 1", "green", "black", 0, 1
        )
        self.button2 = Button(
            self.main_lower_frame, "Quick Operation 2", "green", "black", 0, 2
        )
        self.button3 = Button(
            self.main_lower_frame, "Quick Operation 3", "green", "black", 0, 3
        )
        self.button4 = Button(
            self.main_lower_frame, "Quick Operation 4", "green", "black", 0, 4
        )

        self.cid_entry.grid(row=0, column=0)

        # ***** CHECKBOX BUTTONS *****

        self.checkbox1 = Checkbox(
            self.main_middle_right_frame,
            "Check Me 1",
            "purple",
            "orange",
            1,
            0,
            0,
            0,
            self.checkbox1_variable,
        )
        self.checkbox2 = Checkbox(
            self.main_middle_right_frame,
            "Check Me 2",
            "purple",
            "orange",
            2,
            0,
            0,
            0,
            self.checkbox2_variable,
        )
        self.checkbox3 = Checkbox(
            self.main_middle_right_frame,
            "Check Me 3",
            "purple",
            "orange",
            3,
            0,
            0,
            0,
            self.checkbox3_variable,
        )

        # ***** LISTBOX WITH SCROLLBAR *****

        self.listbox = tk.Listbox(
            self.main_middle_left_frame,
            selectmode="single",
            bd=5,
            selectbackground="orange",
            selectforeground="black",
        )
        self.scrollbar = tk.Scrollbar(
            self.main_middle_left_frame, orient=tk.VERTICAL, command=self.listbox.yview
        )
        self.listbox.configure(yscrollcommand=self.scrollbar.set, font=("Arial", 18))

        self.listbox.grid(row=1, column=0, sticky="nsew")
        self.scrollbar.grid(row=1, column=1, sticky="ns")

        for i in range(100):
            self.listbox.insert(tk.END, f"Item {i}")

        self.root.mainloop()


App()

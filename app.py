import tkinter as tk
from class_button import Button
from class_label import Label
from class_database import Database
from seeder import seed_database
from class_customer import Customer

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    #######################################
    #### ROOT/FRAME SETUPS AND CONFIGS ####
    #######################################

    self.root = tk.Tk()
    self.root.title("Customer Relationship Management Tool")
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
    self.root.rowconfigure(0, weight=2)
    self.root.rowconfigure(1, weight=10)
    self.root.rowconfigure(2, weight=2)

    # ***** FRAMES *****

    self.main_upper_frame = tk.Frame(self.root, bg="black", bd="10", relief="groove")
    self.main_middle_left_frame = tk.Frame(
        self.root, bg="orange", bd="10", relief="groove"
    )
    self.main_middle_right_frame = tk.Frame(
        self.root, bg="black", bd="10", relief="groove"
    )
    self.main_lower_frame = tk.Frame(
        self.root, bg="black", bd="10", relief="groove"
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

    #################
    #### WIDGETS ####
    #################

    # #### FRAME LABELS ####

    self.label1 = Label(self.main_upper_frame, "JC's Customer Management System", "black", "orange", 0, 0, 10, 10, "ew")
    self.label2 = Label(self.main_middle_right_frame, "Customer Information", "black", "orange", 0, 0, 10, 10, "ew")
    self.label3 = Label(self.main_middle_left_frame, "Customer List", "orange", "black", 0, 0, 0, 0, "ew")
    self.label4 = Label(self.main_lower_frame, "Footer Bar", "black", "orange", 0, 0, 10, 10, "ew")

    #### LISTBOX WITH SCROLLBAR ####

    self.listbox = tk.Listbox(self.main_middle_left_frame, selectmode="single", bd=5, selectbackground="white", selectforeground="black")
    self.scrollbar = tk.Scrollbar(self.main_middle_left_frame, orient="vertical", command=self.listbox.yview)
    self.listbox.configure(yscrollcommand=self.scrollbar.set, font=("Arial", 18))

    self.listbox.grid(row=1, column=0, sticky="nsew")
    self.scrollbar.grid(row=1, column=1, sticky="ns")

    #### Sample Customer List ####
    seed_database()
    db = Database()
    customers = db.fetch_customers()
    for customer in customers:
      self.listbox.insert("end", f"{customer.first_name} {customer.last_name}")


    #### CUSTOMER INFORMATION TEXT BOX ####
    self.customer_information = tk.Text(self.main_middle_right_frame, height=10, width=50, font=("Arial", 18))
    self.customer_information.grid(row=1, column=0, padx=50, pady=50, sticky="nsew")

    def show_selected_customer(event):
      selection = self.listbox.curselection()
      self.label2.change_text(f"{customers[selection[0]].first_name} {customers[selection[0]].last_name}")
      self.customer_information.delete("1.0", "end")
      self.customer_information.insert("end", f"{customers[selection[0]].first_name} {customers[selection[0]].last_name}\n{customers[selection[0]].email}\n{customers[selection[0]].cell_phone}\n{customers[selection[0]].city}, {customers[selection[0]].state} {customers[selection[0]].zip_code}")
    
    self.listbox.bind("<<ListboxSelect>>", show_selected_customer)

app = App()
app.mainloop()

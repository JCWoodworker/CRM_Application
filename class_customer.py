import datetime


class Customer:

  def __init__(self, first_name, last_name, cell_phone, email, address, city, state, zip_code):
    self.first_name = first_name
    self.last_name = last_name
    self.cell_phone = cell_phone
    self.email = email
    self.address = address
    self.city = city
    self.state = state
    self.zip_code = zip_code
    self.created_date = datetime.datetime.now().strftime("%m/%d/%Y at %H:%M")

  def get_all_customer_information(self):
    return f"Name: {self.first_name} {self.last_name}\nCell: {self.cell_phone}\nEmail: {self.email}\nAddress: {self.address}, {self.city}, {self.state}, {self.zip_code}\nCustomer Added: {self.created_date}"

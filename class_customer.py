class Customer:

  def __init__(self, id, first_name, last_name, cell_phone, email, street, city, state, zip_code):
    self.id = id
    self.first_name = first_name
    self.last_name = last_name
    self.cell_phone = cell_phone
    self.email = email
    self.street = street
    self.city = city
    self.state = state
    self.zip_code = zip_code

  def __str__(self):
    return f"{self.first_name} {self.last_name} lives at {self.street} in {self.city}, {self.state} {self.zip_code}.  ID #{self.id}."

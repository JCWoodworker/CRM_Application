from class_customer import Customer

john_smith = Customer(
    "John",
    "Smith",
    "555-555-5555",
    "john@fakeemail.com",
    "123 Main St",
    "Anytown",
    "CA",
    "12345",
)

print(john_smith.get_all_customer_information())

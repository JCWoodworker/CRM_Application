from class_database import Database

def seed_database():
  database = Database()
  database.execute_query("DROP TABLE IF EXISTS customers;")
  database.execute_query(
    """
      CREATE TABLE customers (
          id serial PRIMARY KEY,
          first_name varchar(50) NOT NULL,
          last_name varchar(50) NOT NULL,
          cell varchar(50) NOT NULL,
          email varchar(50) NOT NULL,
          street_address varchar(50) NOT NULL,
          city varchar(50) NOT NULL,
          state varchar(50) NOT NULL,
          zip varchar(50) NOT NULL
      );
    """
  )
  database.add_customer(
      "John",
      "Smith",
      "555-555-5555",
      "smith@fake.com",
      "123 Main St",
      "Anytown",
      "CA",
      "12345",
  )
  database.add_customer(
      "Mike",
      "Doe",
      "555-555-5555",
      "doe@fake.com",
      "123 Main St",
      "Anytown",
      "CA",
      "12345",
  )
  database.add_customer(
      "Rob",
      "Docker",
      "555-555-5555",
      "docker@fake.com",
      "123 Main St",
      "Anytown",
      "CA",
      "12345",
  )
  database.add_customer(
      "Amanda",
      "Lane",
      "555-555-5555",
      "lane@fake.com",
      "123 Main St",
      "Anytown",
      "CA",
      "12345",
  )
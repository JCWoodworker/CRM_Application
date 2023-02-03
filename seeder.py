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
          street varchar(50) NOT NULL,
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
      "12 Park Ave",
      "Somwhere",
      "RI",
      "34343",
  )
  database.add_customer(
      "Rob",
      "Docker",
      "555-555-5555",
      "docker@fake.com",
      "44 Mickey Lane",
      "Anotherton",
      "WV",
      "13345",
  )
  database.add_customer(
      "Amanda",
      "Lane",
      "555-555-5555",
      "lane@fake.com",
      "315 March Ave",
      "Oppositeville",
      "MO",
      "69696",
  )
  database.add_customer(
      "Mazie",
      "Sookie",
      "555-555-5555",
      "sookie@fake.com",
      "5 Past St",
      "Anytown",
      "CA",
      "12345",
  )
  database.add_customer(
      "Manny",
      "Jordan",
      "555-555-5555",
      "jordan@fake.com",
      "34 Sommerville Ave",
      "Somwhere",
      "CO",
      "34343",
  )
  database.add_customer(
      "Sammy",
      "Footsmith",
      "555-555-5555",
      "footsmith@fake.com",
      "44 Mickey Lane",
      "Anotherton",
      "TX",
      "13345",
  )
  database.add_customer(
      "Ricky",
      "Connor",
      "555-555-5555",
      "connor@fake.com",
      "342 Sixth Ave",
      "Oppositeville",
      "NY",
      "69696",
  )
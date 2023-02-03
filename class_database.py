import psycopg2
from class_customer import Customer

class Database:
  def __init__(self):
    self.connect_to_database()

  def connect_to_database(self):
    try:
      conn = psycopg2.connect(
          host="127.0.0.1",
          database="pythoncrm",
          user="pythoncrmuser",
          password="pythoncrmpassword",
      )
      print("Connected to database")
      return conn
    except Exception as e:
      print(f"Unable to connect to the database: {e}")
  
  def execute_query(self, query):
    conn = self.connect_to_database()
    cursor = conn.cursor()
    try:
      cursor.execute(query)
      conn.commit()
    except Exception as e:
      print(f"Error executing SQL: {e}")
    finally:
      cursor.close()
      conn.close()
  
  def add_customer(self, first_name, last_name, cell, email, street, city, state, zip):
    conn = self.connect_to_database()
    cursor = conn.cursor()
    try:
      cursor.execute(
          f"""
          INSERT INTO customers (first_name, last_name, cell, email, street, city, state, zip)
          VALUES ('{first_name}', '{last_name}', '{cell}', '{email}', '{street}', '{city}', '{state}', '{zip}');
      """
      )
      conn.commit()
      print(f"Customer {first_name} {last_name} added successfully")
    except Exception as e:
        print(f"Error adding customer: {e}")
    finally:
      cursor.close()
      conn.close()

  def fetch_customers(self):
    conn = self.connect_to_database()
    cursor = conn.cursor()
    try:
      cursor.execute("SELECT * FROM customers;")
      customers = cursor.fetchall()
      customer_objects = []
      for customer in customers:
          customer_objects.append(Customer(*customer))
      return customer_objects
    except Exception as e:
      print(f"Error fetching customers: {e}")
    finally:
      cursor.close()
      conn.close()

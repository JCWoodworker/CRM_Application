import psycopg2

# This module's sole purpose is to test the database connection, create a table, and add some data to it


def connect_to_database():
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


def create_table(table_name):
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        cursor.execute(
            f"""
            CREATE TABLE {table_name} (
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
        conn.commit()
        print(f"Table '{table_name}' created successfully")
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        cursor.close()
        conn.close()


def drop_table(table_name):
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
        conn.commit()
        print(f"Table '{table_name}' dropped successfully")
    except Exception as e:
        print(f"Error dropping table: {e}")
    finally:
        cursor.close()
        conn.close()


def add_customer(first_name, last_name, cell, email, street_address, city, state, zip):
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        cursor.execute(
            f"""
            INSERT INTO customers (first_name, last_name, cell, email, street_address, city, state, zip)
            VALUES ('{first_name}', '{last_name}', '{cell}', '{email}', '{street_address}', '{city}', '{state}', '{zip}');
        """
        )
        conn.commit()
        print(f"Customer {first_name} {last_name} added successfully")
    except Exception as e:
        print(f"Error adding customer: {e}")
    finally:
        cursor.close()
        conn.close()


drop_table("customers")
create_table("customers")
add_customer(
    "John",
    "Smith",
    "555-555-5555",
    "smith@fake.com",
    "123 Main St",
    "Anytown",
    "CA",
    "12345",
)
add_customer(
    "Jane",
    "Jocker",
    "555-555-5555",
    "jocker@fake.com",
    "123 Main St",
    "Anytown",
    "CA",
    "12345",
)
add_customer(
    "Mike",
    "Doe",
    "555-555-5555",
    "doe@fake.com",
    "123 Main St",
    "Anytown",
    "CA",
    "12345",
)
add_customer(
    "Rob",
    "Docker",
    "555-555-5555",
    "docker@fake.com",
    "123 Main St",
    "Anytown",
    "CA",
    "12345",
)
add_customer(
    "Ray",
    "Rockett",
    "555-555-5555",
    "rockett@fake.com",
    "123 Main St",
    "Anytown",
    "CA",
    "12345",
)
add_customer(
    "Mary",
    "Fine",
    "555-555-5555",
    "fine@fake.com",
    "123 Main St",
    "Anytown",
    "CA",
    "12345",
)
add_customer(
    "Amanda",
    "Lane",
    "555-555-5555",
    "lane@fake.com",
    "123 Main St",
    "Anytown",
    "CA",
    "12345",
)
add_customer(
    "Sally",
    "Sangriaton",
    "555-555-5555",
    "sangriaton@fake.com",
    "123 Main St",
    "Anytown",
    "CA",
    "12345",
)

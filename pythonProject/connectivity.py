import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Tejasvi@25'
)

cursor = conn.cursor()

# Create a new database
cursor.execute("CREATE DATABASE IF NOT EXISTS MyDatabase")

# Select the database to use
cursor.execute("USE MyDatabase")

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employees (
        emp_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        position VARCHAR(255),
        salary DECIMAL(10, 2)
    )
""")

# Insert data into the table
sql_insert_query = "INSERT INTO Employees (name, position, salary) VALUES (%s, %s, %s)"
values_to_insert = [
    ("John Doe", "Software Engineer", 70000.00),
    ("Jane Smith", "Project Manager", 90000.00),
    ("Sam Johnson", "Intern", 30000.00)
]
cursor.executemany(sql_insert_query, values_to_insert)
conn.commit()

# Read data from the table
cursor.execute("SELECT * FROM Employees")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Update a record
sql_update_query = "UPDATE Employees SET salary = %s WHERE emp_id = %s"
cursor.execute(sql_update_query, (75000, 1))
conn.commit()

# Verify the update
cursor.execute("SELECT * FROM Employees WHERE emp_id = 1")
print(cursor.fetchone())

# Delete a record
sql_delete_query = "DELETE FROM Employees WHERE emp_id = %s"
cursor.execute(sql_delete_query, (3,))
conn.commit()

# Verify the deletion
cursor.execute("SELECT * FROM Employees")
for row in cursor.fetchall():
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()

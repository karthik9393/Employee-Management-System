import pyodbc

# Function to establish database connection
def get_db_connection():
    try:
        connection = pyodbc.connect(
            r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
            r"DBQ=C:\Users\sanga\Employee_management_backend\employee_management.accdb;"
        )
        print("Database connected successfully!")
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

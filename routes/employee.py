from flask import Blueprint, request
from database import get_db_connection

employee_bp = Blueprint("employee", __name__)

# Route to fetch all employees
@employee_bp.route("/employees", methods=["GET"])
def get_employees():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            query = "SELECT * FROM [MasterEmployeeRecord]"
            cursor.execute(query)
            rows = cursor.fetchall()

            employees = []
            columns = [column[0] for column in cursor.description]
            for row in rows:
                employees.append(dict(zip(columns, row)))

            return {"employees": employees}, 200
        except Exception as e:
            return {"error": f"Failed to fetch employees: {e}"}, 500
        finally:
            conn.close()
    else:
        return {"error": "Database connection failed!"}, 500

# Route to add a new employee
@employee_bp.route("/employee", methods=["POST"])
def add_employee():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            data = request.json
            query = """
                INSERT INTO [MasterEmployeeRecord] 
                (EmployeeID, FirstName, LastName, CurrentPosition, Email) 
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                data.get("EmployeeID"),
                data.get("FirstName"),
                data.get("LastName"),
                data.get("CurrentPosition"),
                data.get("Email")
            ))
            conn.commit()
            return {"message": "Employee added successfully!"}, 201
        except Exception as e:
            return {"error": f"Failed to add employee: {e}"}, 500
        finally:
            conn.close()
    else:
        return {"error": "Database connection failed!"}, 500

from flask import Blueprint, request
from database import get_db_connection

leave_bp = Blueprint("leave", __name__)

# Route to fetch all leave records
@leave_bp.route("/leaves", methods=["GET"])
def get_leaves():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            query = "SELECT * FROM [LeaveTimeRecord]"
            cursor.execute(query)
            rows = cursor.fetchall()

            leaves = []
            columns = [column[0] for column in cursor.description]
            for row in rows:
                leaves.append(dict(zip(columns, row)))

            return {"leaves": leaves}, 200
        except Exception as e:
            return {"error": f"Failed to fetch leaves: {e}"}, 500
        finally:
            conn.close()
    else:
        return {"error": "Database connection failed!"}, 500

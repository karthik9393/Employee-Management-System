from flask import Blueprint, request
from database import get_db_connection

evaluation_bp = Blueprint("evaluation", __name__)

# Route to fetch all evaluations
@evaluation_bp.route("/evaluations", methods=["GET"])
def get_evaluations():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            query = "SELECT * FROM [EmployeeEvaluations]"
            cursor.execute(query)
            rows = cursor.fetchall()

            evaluations = []
            columns = [column[0] for column in cursor.description]
            for row in rows:
                evaluations.append(dict(zip(columns, row)))

            return {"evaluations": evaluations}, 200
        except Exception as e:
            return {"error": f"Failed to fetch evaluations: {e}"}, 500
        finally:
            conn.close()
    else:
        return {"error": "Database connection failed!"}, 500


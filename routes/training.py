from flask import Blueprint, request
from database import get_db_connection

training_bp = Blueprint("training", __name__)

# Route to fetch all training courses
@training_bp.route("/trainings", methods=["GET"])
def get_trainings():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            query = "SELECT * FROM [TrainingCourses]"
            cursor.execute(query)
            rows = cursor.fetchall()

            trainings = []
            columns = [column[0] for column in cursor.description]
            for row in rows:
                trainings.append(dict(zip(columns, row)))

            return {"trainings": trainings}, 200
        except Exception as e:
            return {"error": f"Failed to fetch trainings: {e}"}, 500
        finally:
            conn.close()
    else:
        return {"error": "Database connection failed!"}, 500

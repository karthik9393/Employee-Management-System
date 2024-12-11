from flask import Flask
from routes.employee import employee_bp
from routes.training import training_bp
from routes.leave import leave_bp
from routes.evaluation import evaluation_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(employee_bp)
app.register_blueprint(training_bp)
app.register_blueprint(leave_bp)
app.register_blueprint(evaluation_bp)

@app.route("/")
def home():
    return "Employee Management System Backend is Running!"

if __name__ == "__main__":
    app.run(debug=True)

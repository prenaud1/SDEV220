# to activate .venv, run the following commands in PowerShell
# 1. Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
# 2. .\.venv\Scripts\Activate.ps1
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)
app.app_context().push()   # this line was missing from the walkthrough, but is necessary now


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route("/")
def index():
    return "Hello!"

@app.route("/drinks")
def get_drinks():
    drinks = Drink.query.all()
    output = []
    for drink in drinks:
        drink_data = {"name": drink.name, "description": drink.description}
        output.append(drink_data)
    return {"drinks": output}

@app.route("/drinks/<id>")
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name, "description": drink.description}

@app.route("/drinks", methods=["POST"])
def add_drink():
    # if using Postman and getting 415 error, be sure to change type from Text to JSON.
    drink = Drink(name=request.json["name"], description=request.json["description"])
    db.session.add(drink)
    db.session.commit()
    return {"id": drink.id}

@app.route("/drinks/<id>", methods=["DELETE"])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error": "not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "yeet!@"}


"""
db.create_all()
drink = Drink(name="Grape Soda", description="Tastes like grapes")
db.session.add(drink)
db.session.commit()
print(Drink.query.all())
"""


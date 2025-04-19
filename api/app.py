# to activate .venv, run the following commands in PowerShell
# 1. Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
# 2. .\.venv\Scripts\Activate.ps1
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db = SQLAlchemy(app)
app.app_context().push()   # this line was missing from the walkthrough, but is necessary now


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100))

    def __repr__(self):
        return f"{self.book_name} by {self.author} published by {self.publisher}"

@app.route("/")
def index():
    return "Hello!"

@app.route("/books")
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {"book_name": book.book_name, "author": book.author, "publisher": book.publisher}
        output.append(book_data)
    return {"books": output}

@app.route("/books/<id>")
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"name": book.book_name, "author": book.author, "publisher": book.publisher}

@app.route("/books", methods=["POST"])
def add_book():
    # if using Postman and getting 415 error, be sure to change type from Text to JSON.
    book = Book(book_name=request.json["book_name"], author=request.json["author"], publisher=request.json["publisher"])
    db.session.add(book)
    db.session.commit()
    return {"id": book.id}

@app.route("/books/<id>", methods=["DELETE"])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "yeet!@"}


"""
db.create_all()
book = Book(book_name="To Catch a Roadrunner", author="W.E. Coyote", publisher="ACME")
db.session.add(book)
db.session.commit()
print(Book.query.all())
"""


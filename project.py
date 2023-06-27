import requests
import json
from datetime import datetime
from cs50 import SQL
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    jsonify,
)
from flask_session import Session
from werkzeug.security import check_password_hash
from functools import wraps

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///frappe.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


# Function to calculate fees, abased on current date
def calculate_due(transaction_id):

    transaction = db.execute("SELECT * FROM transactions WHERE id = ?", transaction_id)[
        0
    ]
    issue_date = datetime.strptime(
        transaction["issue_date"], "%Y-%m-%d %H:%M:%S")
    return_date = datetime.now()
    days_since_return = (return_date - issue_date).days
    due_amount = 20
    due_days = 0
    if days_since_return > 7:
        due_days = days_since_return - 7
    due_amount += due_days * 5
    return (due_amount, due_days)

# For pytest
def days_due_amount(days_since_return):
    due_amount = 20
    due_days = 0
    if days_since_return > 7:
        due_days = days_since_return - 7
    due_amount += due_days * 5
    return (due_amount)

# Home / Books

# Book page
@app.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":

        search_term = request.form.get("query")
        query = f"""
            SELECT *
            FROM books
            WHERE title LIKE '%{search_term}%'
                OR author LIKE '%{search_term}%'
                OR id LIKE '%{search_term}%'
                OR isbn LIKE '%{search_term}%'
        """

        books = db.execute(query)
        title = "Search Result"
    else:
        books = db.execute(
            "SELECT * FROM books ORDER BY date_added DESC LIMIT 10")
        title = "Recently Added Books"
        search_term = ""

    return render_template(
        "home.html", title=title, books=books, search_term=search_term
    )


# Add a book
@app.route("/add_book", methods=["POST"])
def add_book():
    title = request.form["title"]
    authors = request.form["author"]
    isbn = request.form["isbn"]
    publisher = request.form["publisher"]
    num_pages = request.form["pages"]
    num_books = request.form["stock"]
    publication_date = request.form["date"]
    date_of_adding = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    existing_book = db.execute("SELECT * FROM books WHERE isbn = ?", isbn)
    if not existing_book:
        db.execute(
            "INSERT INTO books (title, author, isbn, publisher, pages, stock, date, date_added) VALUES (?, ?, ?, ?, ?, ?,?, ?)",
            title,
            authors,
            isbn,
            publisher,
            num_pages,
            num_books,
            publication_date,
            date_of_adding,
        )
    else:
        db.execute(
            "UPDATE books SET stock = stock + ? WHERE isbn = ?", num_books, isbn)

    return redirect("/")


# Issue a book


@app.route("/issue_book", methods=["POST"])
def issue_book():
    book_id = request.form["book_id"]
    member_id = request.form["member_id"]

    member_exist = db.execute("SELECT * from members where ID = ?", member_id)

    if not member_exist:
        flash("User ID is not valid. ", "red")
    else:
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        transactions = db.execute(
            "SELECT id from transactions WHERE member_id = ? AND status = 'Issued'",
            member_id,
        )

        due = 0
        for i in transactions:
            due += calculate_due(i["id"])[0]

        if due > 500:
            flash("Due is over 500 rupees.", "red")

        else:

            db.execute(
                "INSERT INTO transactions (book_id, member_id, issue_date) VALUES (?, ?, ?)",
                book_id,
                member_id,
                current_date,
            )

            db.execute(
                "UPDATE books SET stock = stock - 1 WHERE id = ?", book_id)

            name = db.execute("SELECT * from members where id = ?", member_id)[0][
                "name"
            ]

            flash(f"Book issued successfully to {name}.", "green")

    return redirect("/")


# Import a book


@app.route("/import_books", methods=["GET", "POST"])
@login_required
def import_books():
    if request.method == "POST":
        data = request.json
        num_books = data.get("numBooks")
        num_books = int(num_books)
        title = data.get("title")
        authors = data.get("authors")
        isbn = data.get("isbn")
        publication_date = data.get("publication_date")
        date_object = datetime.strptime(publication_date, "%m/%d/%Y")
        publication_date = date_object.strftime("%Y-%m-%d")

        publisher = data.get("publisher")
        num_pages = data.get("num_pages")
        date_of_adding = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        existing_book = db.execute("SELECT * FROM books WHERE isbn = ?", isbn)
        try:
            if not existing_book:
                db.execute(
                    "INSERT INTO books (title, author, isbn, publisher, pages, stock, date, date_added) VALUES (?, ?, ?, ?, ?, ?,?, ?)",
                    title,
                    authors,
                    isbn,
                    publisher,
                    num_pages,
                    num_books,
                    publication_date,
                    date_of_adding,
                )
            else:
                db.execute(
                    "UPDATE books SET stock = stock + ? WHERE isbn = ?", num_books, isbn
                )
        except:
            result = {"message": "Error in importing."}
        else:
            result = {"message": "Successfully imported !"}
        finally:
            return result

    return render_template("import_books.html")


# Search from Frappe API


@app.route("/api/search", methods=["GET"])
def search():
    base_url = "https://frappe.io/api/method/frappe-library"
    query_params = request.args.to_dict()

    response = requests.get(base_url, params=query_params)

    # num_pages Fix
    fixed_json = json.loads(response.text.replace("  num_pages", "num_pages"))

    return jsonify(fixed_json), response.status_code


# Members

# Members Page
@app.route("/members", methods=["GET", "POST"])
@login_required
def members():
    if request.method == "POST":
        search_term = request.form.get("query")
        query = f"""
            SELECT *
            FROM members
            WHERE id LIKE '%{search_term}%'
                OR name LIKE '%{search_term}%'
                OR phone LIKE '%{search_term}%'
                OR email LIKE '%{search_term}%'

        """
        members = db.execute(query)
        title = "Search Results"

    else:
        members = db.execute(
            "SELECT * FROM members ORDER BY doj DESC LIMIT 10")
        search_term = ""
        title = "Recent Members"
    try:
        mem_num = db.execute(
            "SELECT * FROM members ORDER BY id DESC LIMIT 1")[0]["id"]
        mem_num = int(mem_num) + 1
    except:
        mem_num = 1

    return render_template(
        "members.html",
        search_term=search_term,
        mem_num=mem_num,
        members=members,
        title=title,
    )


# Add A Member
@app.route("/add_member", methods=["POST"])
def add_member():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]

    date_of_joining = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.execute(
        "INSERT INTO members (name, email, phone, doj) VALUES (?, ?, ?, ?)",
        name,
        email,
        phone,
        date_of_joining,
    )
    return redirect("/members")


# Delete a member
@app.route("/delete_member", methods=["POST"])
def delete_member():
    member_id = int(request.form.get("member_id"))
    try:
        db.execute("DELETE FROM members WHERE id = ?", member_id)
    except:
        flash("Member has books to return.", "red")
    else:
        flash("Member deleted successfully.", "green")
    return redirect("/members")


# Edit Memeber
@app.route("/edit_member", methods=["POST"])
def edit_member():

    member_id = int(request.form["member_id"])
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]

    db.execute(
        "UPDATE members SET name = ?, email = ?, phone = ? WHERE id = ?",
        name,
        email,
        phone,
        member_id,
    )

    return redirect("/members")


# Member Info
@app.route("/member_info/<id>", methods=["GET"])
@login_required
def member_info(id):
    info = db.execute("SELECT * from members WHERE id = ?", id)[0]
    transactions = db.execute(
        "SELECT id from transactions WHERE member_id = ? AND status = 'Issued'", id
    )

    due = 0
    for i in transactions:
        due += calculate_due(i["id"])[0]

    return render_template("member_info.html", due=due, info=info)


# Transaction

# Transaction Page
@app.route("/transactions", methods=["GET", "POST"])
@login_required
def transactions():
    if request.method == "POST":

        search_term = request.form.get("query")
        search_by = request.form.get("search_by")
        query = f""" SELECT t.*, b.title AS book_title, m.name AS member_name
                FROM transactions t
                JOIN books b ON t.book_id = b.id
                JOIN members m ON t.member_id = m.id
                WHERE t.{search_by} LIKE '%{search_term}%'
                """

        transactions = db.execute(query)
        title = "Search Results"

    else:
        transactions = db.execute(
            """SELECT t.*, b.title AS book_title, m.name AS member_name
FROM transactions t
JOIN books b ON t.book_id = b.id
JOIN members m ON t.member_id = m.id
WHERE t.status = 'Issued'
ORDER BY t.issue_date DESC
LIMIT 10;

"""
        )
        title = "Recent Transactions"

    return render_template("transactions.html", title=title, transactions=transactions)


# Return a book
@app.route("/return_book/<id>", methods=["GET"])
def return_book(id):
    book_id = db.execute("SELECT book_id FROM transactions WHERE id = ?", id)[0][
        "book_id"
    ]
    db.execute("UPDATE books SET stock = stock + 1 WHERE id = ?", book_id)
    db.execute(
        "UPDATE transactions SET status = 'Returned', fee_paid = ? WHERE id = ?",
        calculate_due(id)[0],
        id,
    )

    flash("Book returned", "green")
    return redirect("/transactions")


# Fee
@app.route("/fee/<id>", methods=["GET"])
@login_required
def fee(id):
    transaction = db.execute("SELECT * FROM transactions WHERE id = ?", id)[0]
    amount = calculate_due(id)[0]
    due_days = calculate_due(id)[1]
    return render_template(
        "fee.html",
        transaction=transaction,
        amount=amount,
        due_days=due_days,
        due_amount=amount - 20,
    )


# Reports

# Reports Page
@app.route("/reports", methods=["GET"])
@login_required
def reports():
    return render_template("reports.html")


# Top Books API


@app.route("/api/top-books")
def top_books_api():
    book_data = db.execute(
        """SELECT f.book_id, b.title, SUM(f.fee_paid) AS total_fees
FROM transactions f
JOIN books b ON f.book_id = b.id
GROUP BY f.book_id, b.title
ORDER BY total_fees DESC
LIMIT 10;
"""
    )
    return jsonify(book_data)


# Top Paying Member API


@app.route("/api/top-members")
def top_members_api():
    top_paying = db.execute(
        """SELECT m.id,
       m.name,
       SUM(f.fee_paid) AS total_fees
  FROM transactions f
       JOIN
       members m ON f.member_id = m.id
 GROUP BY m.id,
          m.name
 ORDER BY total_fees DESC
 LIMIT 10;
"""
    )
    return jsonify(top_paying)


# MISC

# Login


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if not request.form.get("username"):
            flash("Please Enter Username", "yellow")
            return redirect("/login")

        elif not request.form.get("password"):
            flash("Please Enter Password", "red")
            return redirect("/login")
        username = request.form.get("username").lower().strip()
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        password = request.form.get("password")
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            flash("Invalid username and/or password", "red")
            return redirect("/login")
        session["user_id"] = rows[0]["id"]
        flash("Login Successful, Welcome to BookWise", "green")
        return redirect("/")
    else:
        return render_template("login.html")


# Logout
@app.route("/logout")
def logout():
    # Forget any user_id
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

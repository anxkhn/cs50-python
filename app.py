import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        symbol = request.form.get("symbol").upper()

        if not symbol:
            return apology("Please enter a symbol")

        buffer_stocks = lookup(symbol)

        if not buffer_stocks:
            return apology("Invalid Symbol!")

        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("Please enter a value")

        if shares <= 0:
            return apology("shares must contain positive numbers")

        user_id = session["user_id"]

        user_balance = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

        current_stock_price = buffer_stocks["price"]
        name = buffer_stocks["name"]
        total_shares_bought = current_stock_price * shares
        total_cash_left = user_balance - total_shares_bought

        if total_shares_bought > user_balance:
            return apology("Not enough cash")

        db.execute("UPDATE users SET cash = ? WHERE id = ?", total_cash_left, user_id)

        db.execute("INSERT INTO history (user_id, name, shares, price, type, symbol) VALUES (?, ?, ?, ?, ?, ?)",
                   user_id, name, shares, current_stock_price, "buy", symbol)

        return redirect('/')
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Please enter a symbol.")

        stock = lookup(symbol.upper())

        if not stock:
            return apology("Symbol does not exist!")
        return render_template("quotes_page.html", stock=stock, usd_style=usd)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if (request.method == "POST"):
        username = request.form.get('username')
        password = request.form.get('password')
        reenter = request.form.get('reenter')

        if not username:
            return apology('Please enter username!')
        elif not password:
            return apology('Please enter password!')
        elif not reenter:
            return apology('Please re enter password!')

        if password!= reenter:
            return reenter('Password does not match.')

        hash = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users(username, hash) VALUES (?,?)", username, hash)
            return redirect('/')
        except:
            return apology('Username taken already')
    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")

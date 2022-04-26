import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env 


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_sales")
def get_sales():
    sales = list(mongo.db.sales.find())
    return render_template("sales.html", sales=sales)


@app.route("/register", methods=["GET", "POST"])   
def register():
    if request.method == "POST":
        #check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:

            flash("Username already used")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("dashboard", username=session["user"]))
    return render_template("register.html") 


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "dashboard", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/dashboard/<username>", methods=["GET", "POST"])
def dashboard(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:	
        return render_template("dashboard.html", username=username)	
    return redirect(url_for("login"))    


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/new_sales", methods=["GET", "POST"])
def new_sales():
    if request.method == "POST":
        purchase_approval = "yes" if request.form.get("purchase_approval") else "no"
        sale = {
            "customer_name": request.form.get("customer_name"),
            "sale_amount": request.form.get("sale_amount"),
            "sale_description": request.form.get("sale_description"),
            "close_date": request.form.get("close_date"),
            "purchase_approval": purchase_approval,
            "created_by": session["user"]
        }
        mongo.db.sales.insert_one(sale)
        flash("Congratulations! Sale successfully uploaded!")
        return redirect(url_for("get_sales"))

    return render_template("new_sales.html")    


@app.route("/edit_sale/<sale_id>", methods = ["GET", "POST"])
def edit_sale(sale_id):
    if request.method == "POST":
        purchase_approval = "Yes" if request.form.get("purchase_approval") else "No"
        submit = {
            "customer_name": request.form.get("customer_name"),
            "sale_amount": request.form.get("sale_amount"),
            "sale_description": request.form.get("sale_description"),
            "close_date": request.form.get("close_date"),
            "purchase_approval": purchase_approval,
            "created_by": session["user"]
        }
        mongo.db.sales.replace_one({"_id": ObjectId(sale_id)}, submit)
        flash("Congratulations! Sale successfully edited!")

    sale = mongo.db.sales.find_one({"_id": ObjectId(sale_id)})
    return render_template("edit_sale.html", sale=sale,)


@app.route("/delete_sale/<sale_id>")
def delete_sale(sale_id):
    mongo.db.sales.delete_many({"_id": ObjectId(sale_id)})
    flash("Sale Successfully Deleted")
    return redirect(url_for("get_sales"))


@app.route("/get_users")
def get_users():
    users = list(mongo.db.users.find().sort("username"))
    return render_template("users.html", users=users)


@app.route("/new_user", methods=["GET", "POST"])
def new_user():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:

            flash("Username already used")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        } 
        user = {
            "username": request.form.get("username"), 
            "password": request.form.get("password") 
        }
        mongo.db.users.insert_one(user)
        flash("New User Added")
        return redirect(url_for('get_users'))

    return render_template("new_user.html")


@app.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if request.method == "POST":
        submit = {
            "username": request.form.get("username")
        }
        mongo.db.users.replace_one({"_id": ObjectId(user_id)}, submit)
        flash("User Successfully Updated!")
        return redirect(url_for("get_users"))

    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("edit_user.html", user=user)


@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    flash("User Successfully Deleted")
    return redirect(url_for("get_users"))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


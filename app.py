"""Code credit: the code is written following the Code Institute tutorials."""


import os
from flask import (
    Flask,
    flash,
    render_template,
    redirect,
    request,
    session,
    url_for,
)
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
@app.route("/index")
def index():
    """Navigate to Home page."""
    return render_template("index.html")


@app.route("/get_recipes")
def get_recipes():
    """Navigate to All Recipes page.
    Retrieve recipes data from MongoDB.
    """
    recipes = list(mongo.db.recipes.find())
    return render_template("all_recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    """Allow users to search for recipes."""
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("all_recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Allow users to register an account."""
    if request.method == "POST":
        # Check if username already exists in db"""
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(register)

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Allow users to login."""
    if request.method == "POST":
        # Check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for("profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """Navigate to Profile page."""
    username = mongo.db.users.find_one({"username": session["user"]})[
        "username"
    ]

    if session["user"]:
        # Display all recipes added by that user
        user = mongo.db.users.find_one({"username": session["user"]})
        recipes = mongo.db.recipes.find({"created_by": session["user"]})
        recipes = list(recipes)
        return render_template(
            "profile.html", username=username, recipes=recipes
        )
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """Allow users to logout.
    Remove user from session cookie.
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_new_recipe", methods=["GET", "POST"])
def add_new_recipe():
    """Allow users to add a new recipe."""
    if "user" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "time": request.form.get("time"),
            "servings": request.form.get("servings"),
            "ingredients": request.form.get("ingredients").splitlines(),
            "preparation": request.form.get("preparation").splitlines(),
            "created_by": session["user"],
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("profile", username=session["user"]))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_new_recipe.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """Allow users to edit a recipe."""
    if "user" not in session:
        return redirect(url_for("login"))
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if not recipe:
        return redirect("404.html"), 404
    if recipe["created_by"] != session["user"]:
        return redirect("500.html"), 500
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "time": request.form.get("time"),
            "servings": request.form.get("servings"),
            "ingredients": request.form.get("ingredients").splitlines(),
            "preparation": request.form.get("preparation").splitlines(),
            "created_by": session["user"],
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("profile", username=session["user"]))
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories
    )


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """Allow users to delete a recipe."""
    if "user" not in session:
        return redirect(url_for("login"))
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if not recipe:
        return redirect("404.html"), 404
    if recipe["created_by"] != session["user"]:
        return redirect("index.html")
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("profile", username=session["user"]))


@app.errorhandler(404)
def page_not_found(e):
    """Handle error 404 and display a custom 404 error page.

    Code credit:https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
    """
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Handle error 500 and display custom 500 error page.

    Code credit:https://flask.palletsprojects.com/en/2.0.x/errorhandling/
    """
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=False,
    )

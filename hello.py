from flask import Flask, render_template

# Create a Flask instance, this is how you always start a flask porject
app = Flask(__name__)

# create a route
@app.route("/")

def index():
    first_name = "Janek"
    favorite_pizza = ["Pepperoni", "Morzarella", "Hawaii", 42]
    return render_template("index.html", 
    first_name=first_name,
    favorite_pizza=favorite_pizza)

# new route for users
@app.route("/user/<name>")

def user(name):
   # return "<h2>Hello {}".format(name)
   return render_template("user.html", user_name=name)

# Custom error pages

# Invalid url
@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"), 404

# Internal server error
@app.errorhandler(500)

def page_not_found(e):
    return render_template("500.html"), 500
from flask import Flask, render_template, flash

# Import stuff for WTF
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create a Flask instance, this is how you always start a flask porject
app = Flask(__name__)

# Create placeholder CSRF Token
app.config['SECRET_KEY'] = '123456'

# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

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

# Create Name page
@app.route("/name", methods=["GET","POST"])
def name():
    name = None # Required because the first time you open the page the Field won't be filled
    form = NamerForm()
    #validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash("Form submitted successfully!")
        
    return render_template("name.html", 
        name = name,
        form = form)
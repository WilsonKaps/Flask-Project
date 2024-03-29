from flask import Flask, render_template


# Flask instance
app = Flask(__name__, template_folder=r'C:\Users\wilso\Documents\Pyhton\assignment\templates')


# create route
@app.route('/')
def index():
    return "<h1>Hello!</h1>"

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)


# Error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
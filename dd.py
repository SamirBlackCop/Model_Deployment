from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    name = "Samir"
    return render_template("demo.html", name=name)


app.run(debug=True)

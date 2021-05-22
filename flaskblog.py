from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Samir',
        "title": "Das",
        "content": "story book",
        "date_posted": "02 jan 2020"
    },
    {
        'author': 'Samir2',
        "title": "Das2",
        "content": "story book2",
        "date_posted": "02 jan 2021"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


if __name__ == '__main__':
    app.run(debug=True)

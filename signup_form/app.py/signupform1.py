from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("signupform1_index.html")


@app.route("/signup")
def signup():
    return render_template('signupform1_signup.html')


@app.route("/thankyou")
def thankyou():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('signupform1_thankyou.html', first=first, last=last)

if __name__ == '__main__':
    app.run(debug=True)


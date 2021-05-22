from flask import Flask, render_template, url_for, request
import pickle

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("iris_index.html")


@app.route("/signup")
def signup():
    return render_template('iris_input.html')


@app.route("/calcuate")
def calcuate():
    spl = request.args.get('spl')
    spw = request.args.get('spw')
    ptl = request.args.get('ptl')
    ptw = request.args.get('ptw')

    data = [[float(spl), float(spw), float(ptl), float(ptw)]]

    lg = pickle.load(open('iris_save.pkl', 'rb'))
    # print(lg.predict([[1, 1 ,1, 1]]))
    prediction = lg.predict(data)

    return render_template('iris_calculate.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)

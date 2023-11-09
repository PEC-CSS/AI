from flask import Flask, render_template
from flask import request as req
import numpy as np
import  pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/predict", methods=['GET','POST'])
def predictPrice():
    if req.method =='POST': 
        area = req.form["area"]
        bedroom = req.form["bedrooms"]
        age = req.form["age"]
        data = np.array([area, bedroom, age], dtype=float)
        output = model.predict([data])

    return render_template("index.html", result = output)

if __name__=="__main__":
    app.run(debug=True, port=5500)
import pickle
from flask import Flask, request, app, jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__) #starting point the application
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scalar.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods = ['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    values = np.array(list(data.values())).reshape(1, -1)
    print(values)
    new_data = scalar.transform(values)
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scalar.transform(np.array(data).reshape(1,-1)) #reshaping to 2D array
    print(final_input)
    output = regmodel.predict(final_input)[0] #taking the 1st value after reshape
    return render_template("home.html", prediction_text=f"The House price(in $100,000s) prediction is {output}")


if __name__ == "__main__":
    app.run(debug=True)
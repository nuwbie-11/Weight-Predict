from flask import render_template, request, jsonify
import numpy as np
import joblib

def about():
    return "Hello"
    # return render_template("about.html")


def home():

    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        feats = dict(request.form).values()
        feats = np.array([float(x) for x in feats])
        # return f"{feats}"
        model = joblib.load("model/Weight-prediction-using-Linear-regression.pkl")
        gender = "Female" if feats[0] == 0 else "Male"
        height = feats[1] 
        result = model.predict([feats])
        result = f"Around {result[0]:1f}"
        return render_template('index.html', result=result,gender=gender,height=height)

      
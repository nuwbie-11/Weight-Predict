from flask import render_template, request, jsonify

def about():
    return render_template("about.html")


def home():
    return render_template("index.html")
      
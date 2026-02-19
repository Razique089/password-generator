from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""

    if request.method == "POST":
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "!#$%&()*+"

        nl = int(request.form["letters"])
        ns = int(request.form["symbols"])
        nn = int(request.form["numbers"])

        pwd_list = []

        for i in range(nl):
            pwd_list.append(random.choice(letters))
        for i in range(ns):
            pwd_list.append(random.choice(symbols))
        for i in range(nn):
            pwd_list.append(random.choice(numbers))

        random.shuffle(pwd_list)
        password = "".join(pwd_list)

    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)

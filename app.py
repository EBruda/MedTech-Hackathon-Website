import os
import pandas as pd

from flask import (
    Flask,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)

app = Flask(__name__)


@app.route("/")
def index():
    print("Request for index page received")
    return render_template("index.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.route("/info", methods=["POST"])
def info():
    name = request.form.get("name")
    print("letter: ", name)
    df = pd.read_csv("baseline.csv")
    letter_row = df.index[df['Letter'] == name].tolist()
    print(letter_row)
    if (len(letter_row) > 0):
        pot1 = df['Pot1'][letter_row[0]]
        pot2 = df['Pot2'][letter_row[0]]
        return render_template("info.html", letter=name, exp1=pot1, exp2=pot2)



if __name__ == "__main__":
    app.run()

from flask import redirect, request, render_template, url_for, Flask, session
from flask_session import Session

from fibonacci import calculate_fibonacci

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def homepage():
    return render_template("homepage.html", display=False)


@app.route("/info")
def info():
    return render_template("info.html")


@app.route("/result", methods=["POST"])
def result():
    fib_index_to_calculate = request.form.get("index")
    if not fib_index_to_calculate:
        return redirect("/")
    if not session.get("dictus"):
        tutego = {}
    else:
        tutego = session["dictus"]
    calculated_fib, new_calculations = calculate_fibonacci(int(fib_index_to_calculate), tutego)
    session["dictus"] = new_calculations
    # dictus[int(fib_index_to_calculate)] = calculated_fib
    return render_template("homepage.html", fib_num=calculated_fib, user_input=fib_index_to_calculate, dictus=session["dictus"], display=True)


if __name__ == '__main__':
    app.run(debug=True)

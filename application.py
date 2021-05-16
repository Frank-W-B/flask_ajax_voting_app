from flask import Flask, render_template

app = Flask(__name__)
votes = 0

@app.route("/")
def index():
    return render_template("index.html", votes=votes)


if __name__ == '__main__':
    app.run(debug=True)

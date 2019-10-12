from flask import Flask, render_template

application = app = Flask(__name__)

@app.route("/")
def home():
    print("test")
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask

# teste

#__name__ = "__main___"
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/about")
def about():
    return "Pagina sobre"

if __name__ == "__main__":
    app.run(debug=True)
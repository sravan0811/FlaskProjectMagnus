from flask import Flask
app = Flask(__name__)

@app.route("/home/<name>")
def home(name):
    return "Hello, "+name+" Welcome to Web Application using Flask Framework"


def help():
    return "This is Help Page"

app.add_url_rule("/help","help",help)

if __name__ == '__main__':
    app.run(debug=True)
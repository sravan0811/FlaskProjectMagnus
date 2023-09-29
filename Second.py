from flask import *
app = Flask(__name__)

@app.route('/<fname>')
def home(fname):
    return render_template('home.html',name=fname)

if __name__ == '__main__':
    app.run(debug=True)
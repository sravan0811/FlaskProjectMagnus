from flask import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Home.html")
@app.route('/register')
def regsiter():
    return render_template('Register.html')

@app.route('/success',methods=['POST','GET'])
def success():
    if request.method =='POST':
        out = request.form
        return render_template('out.html',output=out)

if __name__ == '__main__':
    app.run(debug=True)
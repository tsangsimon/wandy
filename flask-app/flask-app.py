from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hello')
def hello():
    return render_template("hello.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

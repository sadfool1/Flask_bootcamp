from flask import Flask

app = Flask (__name__)

@app.route('/') #the key routing is this decorator
def index():
    return '<h1> Hello Puppy!! </h1>'


if __name__ == '__main__':
    app.run(debug=True)

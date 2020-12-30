from flask import Flask

app = Flask (__name__)

@app.route('/') #the key routing is this decorator
def index(): #127.0.0.1:5000
    return '<h1> Hello Puppy!! </h1>'

@app.route('/information') #127.0.0.1:5000/information
def info():
    return '<h1> Puppies are cute! </h1>'




if __name__ == '__main__':
    app.run(debug=True)

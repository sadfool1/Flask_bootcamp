from flask import Flask

app = Flask (__name__)

@app.route('/') #the key routing is this decorator
def index(): #127.0.0.1:5000
    return '<h1> Hello Puppy!! </h1>'

@app.route('/information') #127.0.0.1:5000/information
def info():
    return '<h1> Puppies are cute! </h1>'

@app.route('/some_page/<name>') #dynamic routing using a variable
def puppy(name): #name is a variable
    # Basic dynamic route with a var )in this case, <name> is the puppy name.
    return '<h1> This is a page for {} </h1>'.format(name[100]) #upper attribute will uppercase the name


if __name__ == '__main__':
    app.run(debug=True)

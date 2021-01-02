from flask import Flask, render_template

app = Flask (__name__)

@app.route('/') #the key routing is this decorator
def index(): #127.0.0.1:5000
    name = "Jose"
    letters = list(name)

    my_friends = {'friend': 'John'}
    return render_template('home.html', name = name, letters = letters, my_friends = my_friends)

@app.route('/myfriends/<name>') #127.0.0.1:5000/information
def info(name):
    return render_template('myfriends.html', name = name)



@app.route('/some_page/<name>') #dynamic routing using a variable
def puppy(name): #name is a variable
    # Basic dynamic route with a var )in this case, <name> is the puppy name.
    return '<h1> This is a page for {} </h1>'.format(name[100]) #upper attribute will uppercase the name


if __name__ == '__main__':
    app.run(debug=True)

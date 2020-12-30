from flask import Flask
from flask import request

app = Flask (__name__)

@app.route('/') #the key routing is this decorator
def index(): #127.0.0.1:5000
    return '<h1> Hello Puppy!! </h1>'

@app.route('/puppy_latin/<name>') #dynamic routing using a variable
def puppy(name): #name is a variable

    pupname = ''

    #creating this variable shortens the code
    if name[-1] == 'y':

        pupname = '%s' % (name[:-1]) + ''.join('iful')
    else:
        pupname = '%s' % (name) + ''.join('y')

    return '<h1> This is a page for {} </h1>'.format(pupname) #upper attribute will uppercase the name




if __name__ == '__main__':
    app.run(debug=True)

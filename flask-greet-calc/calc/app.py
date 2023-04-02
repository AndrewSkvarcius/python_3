# Put your app in here.
from flask import Flask, request
from operations import sub, add, mult, div

app = Flask(__name__)

@app.route('/add')
def make_add():
    """Adds A+B """
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    sum = add(a,b)

    return str(sum) 

@app.route('/sub')
def make_sub():
    """subtracts A+B """
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    sum = sub(a,b)

    return str(sum) 

@app.route('/mult')
def make_mult():
    """Multiplies A+B """
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    sum = mult(a,b)

    return str(sum) 

@app.route('/div')
def make_div():
    """Divides A+B """
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    sum = div(a,b)

    return str(sum) 

ops = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}
@app.route('/math/<oper>')
def make_math(oper):
    """Makes Math happen on A+B """
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    sum = ops[oper](a,b)

    return str(sum) 

from flask import Flask, request
from operations import functions

app = Flask(__name__)


@app.route('/add')
def add_num():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"<h1>{functions['add'](a, b)}</h1>"


@app.route('/sub')
def sub_num():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"<h1>{functions['sub'](a, b)}</h1>"


@app.route('/mult')
def mult_num():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"<h1>{functions['mult'](a, b)}</h1>"


@app.route('/div')
def div_num():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"<h1>{functions['div'](a, b)}</h1>"


@app.route('/math/<function>')
def math(function):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    print(functions.get(function))
    function_passed = functions.get(function)
    return f"<h1>{function_passed(a, b)}</h1>"

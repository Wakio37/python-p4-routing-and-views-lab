#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_text(parameter):
    print(parameter)
    return parameter

@app.route('/count/<parameter>')
def count(parameter):
    return '\n'.join([str(i) for i in range(int(parameter))])+'\n'


@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero!'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation!'

    print(f'<p>Result of {num1} {operation} {num2}: {result}</p>')
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)

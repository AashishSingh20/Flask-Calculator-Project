# GET method is the request we send to the server
# POST method is the request we recieve from the server

from flask import Flask,request ,render_template , jsonify

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/math',methods=['POST'])
def math_ops():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if ops == 'add':
            r = num1+num2
            result = f"The summation of {num1} and {num2} is {r}"
        elif ops == 'subtract':
            r = num1-num2
            result = f"The subtraction of {num1} and {num2} is {r}"
        elif ops == 'multiply':
            r = num1*num2
            result = f"The multiplication of {num1} and {num2} is {r}"
        elif ops == 'divide':
            r = num1/num2
            result = f"The division of {num1} and {num2} is {r}"
        elif ops == 'divide':
            if num2 == 0:
                return "Cannot divide by zero"
            r = num1 / num2 

        return render_template('results.html', operation=result, result=r)
    

@app.route('/postman_action',methods=['POST'])   # Used on postman
def math_ops1():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if ops == 'add':
            r = num1+num2
            result = f"The summation of {num1} and {num2} is {r}"
        elif ops == 'subtract':
            r = num1-num2
            result = f"The subtraction of {num1} and {num2} is {r}"
        elif ops == 'multiply':
            r = num1*num2
            result = f"The multiplication of {num1} and {num2} is {r}"
        elif ops == 'divide':
            r = num1/num2
            result = f"The division of {num1} and {num2} is {r}"
        elif ops == 'divide':
            if num2 == 0:
                return "Cannot divide by zero"
            r = num1 / num2
            
        return jsonify(result)
    

if __name__== "__main__":
    app.run(host="0.0.0.0")
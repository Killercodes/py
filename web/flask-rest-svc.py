# Flask-Web-Svc
from flask import Flask
app = Flask(__name__)

@app.route('/<int:num>')
def index(num=1):
    return "Your Python Web Service <hr>Fibonacci("+ str(num) + "): "+ str(fibonacci(num))+ "<hr>Square("+ str(num) + "): "+ str(square(num))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def square(n):
    print ("Calculating for the number %s" %n)
    return n*n

if __name__ == '__main__':
    app.run(debug=True)

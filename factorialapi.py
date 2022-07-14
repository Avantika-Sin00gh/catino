from flask import Flask, jsonify
app=Flask(__name__)

@app.route('/avantika/<int:n>')
def factorial(n):
    factorial=1
    if n < 0:
        print("Sorry, factorial does not exist for negative numbers")
        result={
            "Number": n,
            "Factorial": False,
        }
    elif n == 0:
        print("The factorial of 0 is 1")
        result={
            "Number": n,
            "Factorial": 1,
        }
    else:
        for i in range(1,n + 1):
            factorial = factorial*i
            print("The factorial of",n,"is",factorial)
            result={
                "Number": n,
                "Factorial": factorial,
            }
        return jsonify(result)

if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, jsonify
app=Flask(__name__)

@app.route('/avantika/<int:n>')
def amstrong(n):
    sum=0
    nn=n
    order= len(str(n))
    copy_n=n
    while(n>0):
        digit=n%10
        sum+=digit **order
        n=n//10

        if(sum==copy_n):
            print(f"{copy_n} is an armstrong number")
            result={
                "Number": nn,
                "Armstrong": True,
            }
        else:
            print(f"{copy_n} is not an armstrong number")
            result={
                "Number": nn,
                "Armstrong": False,
            }
        return jsonify(result)

if __name__=="__main__":
    app.run(debug=True)
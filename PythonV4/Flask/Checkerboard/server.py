from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def index():
    return render_template ('index.html', row = 8 , col = 8)

@app.route('/<num>')
def columns(num):
    return render_template ('index.html', row = 8, col = int(num))

@app.route('/<num1>/<num2>')
def rowcolumn(num1,num2):
    return render_template('index.html', row = int(num1), col = int(num2))

@app.route('/<num1>/<num2>/<clr1>/<clr2>') 
def all(num1,num2,clr1,clr2) :
    return render_template('index.html', row = int(num1), col = int(num2), color1 = clr1, color2 = clr2) 


if __name__ == "__main__":
    app.run(debug=True)

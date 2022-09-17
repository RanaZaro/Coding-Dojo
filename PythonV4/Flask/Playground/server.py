
from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def box(number=3,color="#9ec5f8"):
    return render_template("index.html",num=int(number),boxcolor=color)

@app.route('/play/<number>')
def play(number,color="#9ec5f8"):
    return render_template("index.html",num=int(number),boxcolor=color)

@app.route('/play/<number>/<color>')
def play_color(number,color):
    return render_template("index.html",num=int(number),boxcolor=color)

if __name__=="__main__":
    app.run(debug=True)
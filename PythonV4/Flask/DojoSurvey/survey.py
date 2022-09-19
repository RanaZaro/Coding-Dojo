from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('survery.html')

@app.route('/results', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment =  request.form['comment']
    return render_template('results.html', name = name, location = location, language = language, comment = comment)


app.run(debug=True)
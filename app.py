from flask import Flask, render_template, request, flash
import requests
import json

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
     if request.method == 'POST':
        from_currency = request.form['from']
        to_currency = request.form['to']
        amount = request.form['amount']


    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
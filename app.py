from flask import Flask, render_template, request, flash
import requests
import json
from utils import is_valid_currency

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        from_currency = request.form['from']
        to_currency = request.form['to']
        amount = request.form['amount']

        if not is_valid_currency(from_currency) or not is_valid_currency(to_currency):
            flash('Please input valid currency codes', 'error')
            return render_template('index.html')

        try:
            amount = float(amount)
        except ValueError:
            flash('Please input a valid number for amount', 'error')
            return render_template('index.html')
        
        req_url = f'https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}'
        response = requests.get(req_url)

        if response.status_code == 200:
            result = response.json()
            if result['success']:
                conversion_result = round(result['result'], 2)
                flash(f'The converted amount is {conversion_result}', 'success')
            else:
                flash('Error in currency conversion. Please try again', 'error')

        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
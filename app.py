from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    age_years, age_months, age_days = None, None, None
    if request.method == 'POST':
        birth_date_str = request.form['birth_date']
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
        today = datetime.today()
        
        # Calculating years, months, and days
        age_years = today.year - birth_date.year
        age_months = today.month - birth_date.month
        age_days = today.day - birth_date.day
        
        # Adjust for negative days and months
        if age_days < 0:
            age_days += 30  # Roughly adjust to the previous month
            age_months -= 1
        if age_months < 0:
            age_months += 12
            age_years -= 1

    return render_template('index.html', age_years=age_years, age_months=age_months, age_days=age_days)

if __name__ == '__main__':
    app.run(debug=True)

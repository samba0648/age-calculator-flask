from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def get_zodiac_sign(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    return None

def get_nakshatra(day):
    nakshatras = [
        "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashirsha", 
        "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha", 
        "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", 
        "Swati", "Vishakha", "Anuradha", "Jyeshtha", "Mula", 
        "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", 
        "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
    ]
    return nakshatras[day % len(nakshatras)]

@app.route('/', methods=['GET', 'POST'])
def index():
    age_years, age_months, age_days = None, None, None
    birth_date_str, birth_time_str, zodiac_sign, nakshatra = None, None, None, None

    if request.method == 'POST':
        birth_date_str = request.form['birth_date']
        birth_time_str = request.form.get('birth_time', '00:00')
        birth_datetime = datetime.strptime(f"{birth_date_str} {birth_time_str}", '%Y-%m-%d %H:%M')
        today = datetime.today()
        
        # Calculate years, months, and days
        age_years = today.year - birth_datetime.year
        age_months = today.month - birth_datetime.month
        age_days = today.day - birth_datetime.day
        
        # Adjust for negative days and months
        if age_days < 0:
            age_days += 30
            age_months -= 1
        if age_months < 0:
            age_months += 12
            age_years -= 1
        
        # Calculate zodiac sign and nakshatra
        zodiac_sign = get_zodiac_sign(birth_datetime.month, birth_datetime.day)
        nakshatra = get_nakshatra(birth_datetime.day)

    return render_template('index.html', age_years=age_years, age_months=age_months, age_days=age_days,
                           birth_date_str=birth_date_str, birth_time_str=birth_time_str,
                           zodiac_sign=zodiac_sign, nakshatra=nakshatra)

if __name__ == '__main__':
    app.run(debug=True)

# Age Calculator and Astrology Report

A simple, responsive web application that calculates age in years, months, and days and generates astrology reports with zodiac signs and Nakshatra based on the birthdate and time provided. This application is built using **Flask** (a Python web framework) and **Bootstrap** for a responsive design.

## Features

- Calculates and displays age in years, months, and days.
- Generates astrology reports with zodiac sign and Nakshatra
- User-friendly interface with Bootstrap styling.
- Responsive design for mobile, tablet, and desktop views.
- Minimalistic and clean UI for easy use.

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, Bootstrap (for responsiveness and styling)
- **Date Calculations**: Python's `datetime` module

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/samba0648/age-calculator-flask.git
   cd age-calculator-flask
   ```

2. Install dependencies:

   ```bash
   pip install Flask
   ```

### Running the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your browser and go to:

   ```
   http://127.0.0.1:5000
   ```

## File Structure

```
age_calculator/
├── app.py                # Main Flask application
├── templates/
│   └── index.html        # HTML template for the UI
├── static/
│   └── style.css         # Custom CSS (optional)
└── README.md             # Project documentation
```

## Usage

1. Open the application in your browser.
2. Enter your birthdate in the provided input field.
3. Enter your birth time in the time picker. The default is set to 00:00.
4. Click on **Calculate Age and Generate Report** to see the age in years, months, and days.

## Screenshot

![Output](image.png)

## Future Improvements

- **Localization**: Display the output in multiple languages.
- **Enhanced Accuracy**: Improve date calculations for leap years.
- **Animations**: Add animations for smoother transitions.
from flask import Flask, render_template, request
import calendar

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('homepage.html')

@app.route('/huiskalender', methods=['GET'])
def huiskalender():
    year = 2023
    month = 2
    cal = calendar.monthcalendar(year, month)
    return render_template('huiskalender.html', calendar=cal)

def get_event(date):
    # In a real application, this function would retrieve the event
    # corresponding to the selected date from a database or other data source.
    # For now, we'll just return a dummy event.
    return "This is a sample event for {}".format(date)

if __name__ == '__main__':
    app.run(debug=True)

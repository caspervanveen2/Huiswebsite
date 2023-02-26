from flask import Flask, render_template, request
import calendar

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def mycalendar():
    if request.method == 'POST':
        selected_date = request.form['selected_date']
        event = get_event(selected_date)
    else:
        event = ""
    
    year = 2023
    month = 2
    cal = calendar.monthcalendar(year, month)
    
    return render_template('huiskalender.html', calendar=cal, event=event)

def get_event(date):
    # In a real application, this function would retrieve the event
    # corresponding to the selected date from a database or other data source.
    # For now, we'll just return a dummy event.
    return "This is a sample event for {}".format(date)

if __name__ == '__main__':
    app.run(debug=True)
from dbhelper import DBHelper 
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
db = DBHelper()

@app.route('/')
def home():
    try:
        data = db.get_all_inputs()
    except Exception as e:
        print(e)
        data = None 
    return render_template('home.html', data = data)

@app.route('/add', methods = ['POST'])
def add():
    try:
        data = request.form.get('userinput')
        db.add_input(data)
    except Exception as e:
        print(e)
    return home()

@app.route('/clear')
def clear():
    try:
        db.clear_all()
    except Exception as e:
        print(e)
    return home()

@app.route("/submitcrime", methods = ['POST'])
def submitcrime():
    category = request.form.get('category')
    date = request.form.get('date')
    latitude = float(request.form.get("latitude"))
    longitude = float(request.form.get("longitude"))
    description = request.form.get('description')
    db.add_input(category, date, latitude, longitude, description,datetime.now())
    return home()

if __name__ == '__main__':
    app.run(debug=True)
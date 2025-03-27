from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

doctors = {
    "allergist": ["Dr. Pawan", "Dr. Gupta"],
    "anesthesiologist": ["Dr. Ram", "Dr. Anjali"],
    "cardiologist": ["Dr. Pradeep", "Dr. Jain"],
    "dermatologist": ["Dr. Bhati", "Dr. Arti"],
    "endocrinologist": ["Dr. Shiv", "Dr. Amit"],
    "orthopedic": ["Dr. Rakhi", "Dr. Aditya"],
    "gynaecologist": ["Dr. Chandni", "Dr. Ankit"],
    "psychiatrist": ["Dr. Navin", "Dr. Ravi"],
    "radiologist": ["Dr. Sudhir", "Dr. Ajay"],
    "urologist": ["Dr. Wasim", "Dr. Singh"],
    "surgeon": ["Dr. Anurag", "Dr. Ashish"],
    "neurologist": ["Dr. Raj", "Dr. Mohit"],
    "oncologist": ["Dr. Rajesh", "Dr. Suresh"]
}
USERNAME = "webx"
PASSWORD = "admin"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if not session.get('logged_in'):
    
        return redirect(url_for('login'))

    if request.method == 'POST':
        fullname = request.form.get('fullname', 'Anonymous')
        age = request.form.get('years', 'N/A')
        NO = request.form.get('NO', 'N/A')
        specialist = request.form.get('specialist')
        appointment_date = request.form.get('appointment_date')

        if not specialist or specialist not in doctors:
            return "Invalid specialist selection", 400
        
        assigned_doctor = random.choice(doctors[specialist])
    
    
    
        return render_template('result.html', fullname=fullname, age=age, doctor=assigned_doctor, appointment_date=appointment_date,NO=NO)
    



    return render_template('index.html', doctors=doctors)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
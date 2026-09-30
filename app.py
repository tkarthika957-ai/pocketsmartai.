from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Form details get pannudhal
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Registration success aana udane Login page-ku redirect pannuvom
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Login success aana udane Dashboard-ku redirect pannuvom
        return redirect(url_for('dashboard'))
        
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

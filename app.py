from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'pocketsmart_secret_key'

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Registration details get பண்ணி Login பக்கம் அனுப்பிடும்
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Login சரியானதும் Dashboard பக்கத்திற்கு போகும்
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/home_planner', methods=['GET', 'POST'])
def home_planner():
    if request.method == 'POST':
        # Form submit பண்ணும்போது தேவையா விவரங்களை இங்கு சேர்க்கலாம்
        pass
    return render_template('home_planner.html')

if __name__ == '__main__':
    app.run(debug=True)

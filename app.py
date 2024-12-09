from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flashing messages

# Predefined username and password for simplicity
valid_username = "husnul"
valid_password = "securepassword"

# Route for Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Route for About Page with login required
@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == valid_username and password == valid_password:
            return render_template('about.html')
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

# Route for Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# Route for Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

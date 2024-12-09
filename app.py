from flask import Flask, render_template

app = Flask(__name__)

# Route for Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Route for About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for Fakta Dunia Page
@app.route('/fakta-dunia')
def fakta_dunia():
    return render_template('fakta_dunia.html')

# Route for Kutipan Inspiratif Page
@app.route('/kutipan-inspiratif')
def kutipan_inspiratif():
    return render_template('kutipan_inspiratif.html')

# Route for Ide Kreatif Page
@app.route('/ide-kreatif')
def ide_kreatif():
    return render_template('ide_kreatif.html')

# Route for Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

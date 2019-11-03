from flask import render_template, request, flash, redirect
from flask import Flask

# from app import app

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/family')
def family():
    return render_template('family.html')


@app.route('/family', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/tokyo')

def primeira():
    return render_template('tokyo.html')

@app.route('/kyoto')

def segunda():
    return render_template('kyoto.html')

@app.route('/osaka')

def terceira():
    return render_template('osaka.html')

@app.route('/okinawa')

def quarta():
    return render_template('okinawa.html')

if __name__ == '__main__':
    app.run(debug=True)
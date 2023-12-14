# api_gateway.py

from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    # Your home page logic
    return render_template('homepage.html')

@app.route('/apod')
def redirect_to_apod():
    # Redirect the request to the APOD microservice
    return redirect('http://127.0.0.1:5002/apod')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

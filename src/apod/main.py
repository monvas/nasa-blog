from flask import Flask, render_template, redirect
import requests
import os

app = Flask(__name__)

# NASA APOD API endpoint
NASA_APOD_API_URL = "https://api.nasa.gov/planetary/apod"

# NASA API Key (Replace 'YOUR_API_KEY' with your actual API key)
import os

NASA_API_KEY = os.environ.get('API_KEY')


@app.route("/apod", methods=["GET"])
def get_apod():
    # Construct the API request URL with the API key
    api_url = f"{NASA_APOD_API_URL}?api_key={NASA_API_KEY}"

    try:
        # Make a request to the NASA APOD API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        apod_data = response.json()

        # Render the HTML template with dynamic data
        return render_template("index.html", apod_data=apod_data)

    except requests.exceptions.RequestException as e:
        # Handle request errors
        return render_template("error.html", error=str(e)), 500


@app.route('/')
def redirect_to_home():
    # Redirect the request to the gateway microservice
    return redirect('http://127.0.0.1:8080')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
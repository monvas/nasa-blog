from flask import Flask, render_template, redirect, request
import requests
import os

app = Flask(__name__)

# NASA APOD API endpoint
NASA_APOD_API_URL = "https://api.nasa.gov/planetary/apod"
NASA_EARTH_IMAGERY_API_URL = "https://api.nasa.gov/planetary/earth/assets"

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

@app.route('/earth_assets', methods=['GET', 'POST'])
def earth_imagery():
    if request.method == 'POST':
        latitude = request.form.get('latitude', '')
        longitude = request.form.get('longitude', '')
        date = request.form.get('date', '')

        # Make a request to the NASA API
        api_url = f'{NASA_EARTH_IMAGERY_API_URL}?lon={longitude}&lat={latitude}&date={date}&dim=0.15&api_key={NASA_API_KEY}'
        response = requests.get(api_url)

        try:
            data = response.json()
            image_url = data['url']

            return render_template('earth_assets.html', image_url=image_url)

        except requests.exceptions.RequestException as e:
            return f'Error: {e}'

    return render_template('earth_assets_form.html')


@app.route('/')
def redirect_to_home():
    # Redirect the request to the gateway microservice
    return redirect('http://127.0.0.1:8080')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
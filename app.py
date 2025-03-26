import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default_secret_key")

@app.route('/')
def index():
    # Get API key from environment variable
    api_key = os.environ.get("WEATHER_API_KEY", "")
    return render_template('index.html', api_key=api_key)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

from flask import Flask, render_template
import os


app = Flask(__name__)

@app.route('/')
def index():
    target_url = 'https://chat.openai.com/'  # Replace with the actual URL
    return render_template('index.html', target_url=target_url)

if __name__ == '__main__':
    # Get the port number from the PORT environment variable, default to 10000
    port = int(os.environ.get('PORT', 10000))
    # Run the Flask app on 0.0.0.0 (all available network interfaces) at the specified port
    app.run(host='0.0.0.0', port=port)

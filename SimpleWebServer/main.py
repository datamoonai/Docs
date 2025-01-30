# Create a Flask application
from flask import Flask, request
app = Flask(__name__)

# Define a route for the root URL
@app.route('/test', methods=['POST'])
def test():
    print(request.args)
    return 'Hello, World!'

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
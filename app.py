from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/oauth2/callback')
def oauth2callback():
    return 'This is the callback page!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
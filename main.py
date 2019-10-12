from flask import Flask
app = Flask(__name__)


@app.route('/')
def home_page():
    return 'This is a simple Web Application based on python flask. '

if __name__ == '__main__':
    app.run()

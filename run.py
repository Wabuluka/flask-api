from api.views import app
from flask import jsonify

@app.route('/')
def home():
    return jsonify({'Welcome: Hi there this is my very first Flask-API applcation'})

if __name__ == '__main__':
    app.run(debug = True)

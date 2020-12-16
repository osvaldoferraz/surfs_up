from flask import Flask
app = Flask(__name__)
@app.route('/')
def wife():
    return 'Dani'



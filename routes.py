from flask import Flask, render_template, url_for

app = Flask(__name__)
# instantiating a flask object


# make the function http callable using a decorator
# route is a method

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/lisa/')
def lisa():
    return render_template('lisa.html')

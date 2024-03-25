from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


# instantiating a flask object


# make the function http callable using a decorator
# route is a method

@app.route('/')
def home():
    return render_template('index.html', title='Home')


@app.route('/lisa/')
def lisa():
    return render_template('lisa.html')


@app.route('/Bart/')
def bart():
    return render_template('bart.html')


if __name__ == "__main__":
    app.run(debug=True)

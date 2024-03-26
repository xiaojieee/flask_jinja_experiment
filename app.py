from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


# instantiating a flask object


# make the function http callable using a decorator
# route is a method

@app.route('/')
def home():
    return render_template('home.html', title='Home')


@app.route('/about/')
def about():
    return render_template('about.html', title='About')


@app.route('/lisa/')
def lisa():
    return render_template('lisa.html', title='Lisa')


@app.route('/bart/')
def bart():
    return render_template('bart.html', title='Bart')


@app.route('/homer/')
def homer():
    return render_template('homer.html', title='Homer')


if __name__ == "__main__":
    app.run(debug=True)

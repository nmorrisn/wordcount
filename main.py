from flask import Flask, render_template, flash, request
from flask_wtf import Form
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import random
import re

app = Flask(__name__)
app.secret_key = str(random.randint(1,1000000000000000))

class ReusableForm(Form):
    words = TextAreaField('Words')
    submit = SubmitField("Get Count")
    results = StringField("Count")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/count", methods=['GET', 'POST'])
def count():
    form = ReusableForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required!')
            return render_template('count.html', form=form)
        else:
            words = form.words.data
            print(words)
            x = re.split("\s", words)
            form.results.data = len(x)
            form.process()
            return render_template('results.html', form=form)
    elif request.method == 'GET':
        return render_template('count.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

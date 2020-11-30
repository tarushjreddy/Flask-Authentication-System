import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, Response, request, redirect,  url_for
print("omsairam")


app = Flask(__name__, static_url_path='')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
db = SQLAlchemy(app)


class LoginCred(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.String(20), nullable=False,
                         )
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)


@app.route("/sign", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        post_name = request.form['name']
        post_password = request.form['password']
        post_email = request.form['email']
        new_post = LoginCred(
            name=post_name, email=post_email, password=post_password)
        db.session.add(new_post)
        db.session.commit()
        return render_template('pagetwo.html', posts=new_post)
    else:
        return render_template('signup.html')


def validation(email, password):

    for i in range(5):
        print(i)
        post = LoginCred.query.all()[i]
        if email == post.email and password == post.password:
            return "pass"


@app.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']

        password = request.form['password']
        validation(email, password)

        return "pass"

    else:

        return render_template('pagetwo.html')


if __name__ == "__main__":
    app.run(debug=True)

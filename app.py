from flask import Flask, redirect, url_for, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from wtforms_validators import AlphaNumeric
import os
from itsdangerous import TimedSerializer as TimedSerializer

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()], render_kw={"placeholder": "Email"})

    username = StringField("Username", validators=[DataRequired(), AlphaNumeric()], render_kw={"placeholder": "Username"})

    password_hash = PasswordField('Password', validators=[DataRequired(), AlphaNumeric(), EqualTo('password_hash2', message='Passwords Must Match!')], render_kw={"placeholder": "Password"})

    password_hash2 = PasswordField('Confirm Password', validators=[DataRequired(), AlphaNumeric()], render_kw={"placeholder": "Confirm Password"})

    submit = SubmitField('Register')

class LoginForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired(), AlphaNumeric()], render_kw={"placeholder": "Username"})

	password_hash = PasswordField("Password", validators=[DataRequired(), AlphaNumeric()], render_kw={"placeholder": "Password"})

	submit = SubmitField("Submit")
        
class ResetRequestForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()], render_kw={"placeholder": "Email"})

    submit = SubmitField('Request Password Reset')

        
class ResetPasswordForm(FlaskForm):
    password_hash = PasswordField('Password', validators=[DataRequired(), AlphaNumeric(), EqualTo('password_hash2', message='Passwords Must Match!')], render_kw={"placeholder": "Password"})

    password_hash2 = PasswordField('Confirm Password', validators=[DataRequired(), AlphaNumeric()], render_kw={"placeholder": "Confirm Password"})

    submit = SubmitField('Reset Password')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/input", methods=["GET", "POST"])
def input():
    if request.method == 'POST':
        return render_template('resultpage.html')
    return render_template("input.html")

@app.route("/models")
def models():
    return render_template("models.html")

@app.route("/miRNA")
def miRNA():
    return render_template("miRNA.html")

@app.route("/tutorial")
def tutorial():
    return render_template("tutorial.html")

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    return render_template("404.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    return render_template("404.html")

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    flash('Successfully logged out.')
    return redirect(url_for('signin'))

@app.route("/breast")
def breast():
    return render_template("breast.html")

@app.route("/kidney")
def kidney():
    return render_template("kidney.html")

@app.route("/lung")
def lung():
    return render_template("lung.html")

@app.route("/multiclass")
def multiclass():
    return render_template("multiclass.html")


@app.errorhandler(404)
def pagenotfound(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def servererror(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug=True)
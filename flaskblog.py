import app as app
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect

app.config['SECRET_KEY'] = "fsdffsd"
app.config['WTF_CSRF_SECRET_KEY'] = "DSFSDFS"


@app.route("/")
@app.route("/home")
def home():
    posts = [
        {
            'author': 'Andrew Odongo',
            'title': 'Blog Post 1',
            'content': 'First content',
            'date_posted': 'February 16, 2020'
        },
        {
            'author': 'Joyce Maya',
            'title': 'Blog Post 2',
            'content': 'Second content',
            'date_posted': 'February 17, 2020'
        }]
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for{form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', forms=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

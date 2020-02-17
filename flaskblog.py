from flask import Flask, render_template,url_for
from forms import RegistrationForm, LoginForm


app. config['SECRET_KEY'] = '5058drew40'
app = Flask(__name__)

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
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form =RegistrationForm()
    return render_template('register.html', title='Register', forms=form)

@app.route("/login")
def login():
    form =LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

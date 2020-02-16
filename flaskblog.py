from flask import Flask,render_template
app = Flask(__name__)


posts = [
    {
       'author':'Andrew Odongo',
       'title': 'Blog Post 1',
       'content': 'First content',
       'date_posted': 'February 16, 2020' 
    },
       {
       'author':'Joyce Maya',
       'title': 'Blog Post 2',
       'content': 'Sescond content',
       'date_posted': 'February 17, 2020' 
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)

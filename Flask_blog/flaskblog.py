from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Darlon',
        'title': 'Post 01',
        'content': 'Conteúdo do Post 01',
        'date_posted': '02/05/2024'
    },
    {
        'author': 'Vasata',
        'title': 'Post 02',
        'content': 'Conteúdo do Post 02',
        'date_posted': '17/06/2024'
    }
    
]

@app.route("/")
@app.route("/home")
def home():
    # return "<h1> Home Page<h1>"
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    # return "<h1> About Page<h1>"
    return render_template('about.html', title='About')
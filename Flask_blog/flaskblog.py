from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '1a416b55cf164611b598ff2c9414899a'

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
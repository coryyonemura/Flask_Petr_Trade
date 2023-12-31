from flask import render_template, url_for, flash, redirect
from petrTrade import app
from petrTrade.forms import RegistrationForm, LoginForm

posts = [
    {
        'author':'Cory Yonemura',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'September 27th, 2023'
    },
    {
        'author':'Gavin Yonemura',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': 'September 28th, 2023'
     }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == "password":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

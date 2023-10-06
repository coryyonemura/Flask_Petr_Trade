from flask import Flask, render_template, url_for

app = Flask(__name__)


posts = [
    {
        'author':'Cory Yonemura',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'September 27th, 2023'
    },
    {'author':'Gavin Yonemura',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': 'September 28th, 2023'
     }
]

@app.route('/')
def home():  # put application's code here
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)

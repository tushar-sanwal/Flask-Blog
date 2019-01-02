from flask import Flask, render_template, url_for, flash, redirect
from forms import Registration, Login

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b41b4b321973e48b8de1f41bd97d073b'

posts = [
    {
        'author': 'Tushar',
        'title': 'Blog 1',
        'content': 'My First post',
        'date_posted': 'April 1, 2019'
    },
    {
        'author': 'Tushar',
        'title': 'Blog 2',
        'content': 'My Second post',
        'date_posted': 'April 1, 2018'
    }
]

@app.route('/home')
def home():
    return  render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return  render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        flash(f'Account created {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        flash(f'login successfully! Welcome back', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run()

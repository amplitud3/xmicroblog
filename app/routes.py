from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Mark'}
    posts = [
        { 
            'author': {'username': 'Amaan'},
            'body': 'Beautiful day in portland!'
        },

        {
            'author': {'username': 'Nived'},
            'body': 'The Avengers movie was so cool!'
        },

        {  
            'author':{'username': 'Adith'},
            'body': 'Goa is a beautiful place'
        }    
            ]
    return render_template('index.html', title='Home', user=user,posts=posts)


from flask import render_template
from app import app
from .request import get_sources


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    business_source = get_sources()
    
    # print(business_source)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html',business_sources = business_source)

@app.route('/articles/<int:article_id>')
def articles(article_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('articles.html',id = article_id)


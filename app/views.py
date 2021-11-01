from flask import render_template
from app import app
from .request import get_sources

# # Views
# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     # message = 'Hello World'
#     sports source=get_sources()
#     title = 'Home - Welcome to The Best News Articles Preview Website'
#     return render_template('index.html',sources=source)

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    business_source = get_sources()
    # entertainment_source = get_sources('entertainment')
    # print(business_source)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html',business_sources = business_source)

@app.route('/articles/<int:article_id>')
def articles(article_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('articles.html',id = article_id)

# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     # Getting popular movie
#     business_source = get_sources('business')
#     entertainment_sources = get_sources('entertainment')
#     general_sources = get_sources('general')
#     title = 'Home - Welcome to The best Movie Review Website Online'
#     return render_template('index.html', title = title, business = business_source, entertainment = entertainment_sources, general = general_sources )
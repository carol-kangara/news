from flask import render_template
from . import main
from ..request import get_sources, get_articles
main.route('/')
def index():
    '''
    view root page that rendes the idex.html template and its data
    '''
    general_categories = get_sources('general')
    title='Latest news hub'
    return render_template('index.html',title=title,general = general_categories)

@main.route('/newsarticle/<id>')
def newsarticle(id):

    '''
    View article page function that returns the article details page and its data
    '''
    articles_items = get_articles(id)
    title = f'{id} | Latest news hub'
    return render_template('newsarticle.html',title = title,articles = articles_items) 

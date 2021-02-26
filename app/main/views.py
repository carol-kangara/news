from flask import render_template

app.route('/')
def index():
    '''
    view root page that rendes the idex.html template and its data
    '''
    title='Latest news hub'
    return render_template('index.html,title=title')
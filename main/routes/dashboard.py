import flask
from main import app, login_required

@app.route('/dashboard')
@login_required
def dashboard():
    #print("is dashboard: ", flask.session.get('username'))
    #return flask.render_template('dashboard.html',session=flask.session)
    return flask.render_template('dashboard.html', this_page='Dashboard')

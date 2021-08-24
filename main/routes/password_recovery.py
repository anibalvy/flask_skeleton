import flask
from main import app, db_pool, pg
from main.forms.auth import FormLogin



@app.route('/password_recovery')
def password_recovery():
    # initializing login data
    login_form = FormLogin()
#    try: 
#        db_conn = db_pool.getconn() 
#        if (db_conn):
#            print('connection db successfully')
#            db_pool.putconn(db_conn)
#    except (Exception, pg.DatabaseError , error) as error:
#        print('connection error', error)
    return flask.render_template('password_recovery.html', login_form=login_form)

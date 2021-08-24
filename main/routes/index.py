import flask
#from main import app #, db_pool, pg
from main import app 
from main.forms.auth import FormLogin



@app.route('/')
def index():
    # initializing login data
    login_form = FormLogin()
#    try: 
#        db_conn = db_pool.getconn() 
#        if (db_conn):
#            print('connection db successfully')
#            db_pool.putconn(db_conn)
#    except (Exception, pg.DatabaseError , error) as error:
#        print('connection error', error)
    return flask.render_template('index.html', login_form=login_form)

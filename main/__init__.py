import flask
import psycopg2 as pg
from psycopg2 import pool
from functools import wraps
from .config import Config
 
try:
    db_pool = pg.pool.SimpleConnectionPool(
			1,10,
            user=Config.POSTGRES_USER,
            password=Config.POSTGRES_PASSWORD,
            host='127.0.0.1',
            port=Config.POSTGRES_PORT,
            database=Config.POSTGRES_DB
            )
    if (db_pool):
        print('conection successfully to PGDB')

except (Exception, pg.DatabaseError) as error:
    print('PGDB conection error', error)

finally:
    # closing database connection.
    # use closeall() method to close all the active connection if you want to turn of the application
    if db_pool:
        db_pool.closeall
    print("PostgreSQL connection pool is closed")

app = flask.Flask(__name__)
#app.config['SECRET_KEY'] = Config.SECRET_KEY
app.config.from_object(Config)
#login_manager = flask_login.LoginManager(app)
#login_manager.login_view = "login_page"
#login_manager.login_view = "login"
#login_manager.login_message_category = "info"
#login_manager.login_message = "Please log in!"

#def is_autenticated(fn):
def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("is auth: ", flask.session.get('username'))
        if not  flask.session.get('username') :
            flask.flash("Please log in first")
            return flask.redirect(flask.url_for('login'))
        return fn(*args, **kwargs)
    return wrapper


from main import routes 


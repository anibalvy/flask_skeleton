from main import db_pool, pg
import flask


def user_validation(username, password):
    try:
        if (db_pool):
            print('validating user to PGDB')
        # get Connection from pool
        db_conn = db_pool.getconn()
        if (db_conn):
            print('connected to pool' )
            db_cur = db_conn.cursor()
            db_cur.execute("select fn_user_validate( %s, %s);",  (username, password));
            resultado = db_cur.fetchall()
            print('from db: ' ,resultado[0][0])
            db_cur.close()
            # Return connection back to pool
            db_pool.putconn(db_conn)
            print('connection returned to pool')
            return resultado[0][0]

    except (Exception, pg.DatabaseError) as error:
        print('PGDB conection error: ', error)
        return False
    return False


def user_by_id(user_id):
    try:
        if (db_pool):
            print('user_by_id PGDB')
        # get Connection from pool
        db_conn = db_pool.getconn()
        if (db_conn):
            print('connected to pool' )
            db_cur = db_conn.cursor()
            db_cur.execute("select fn_user_by_id( %s );",  (user_id,));
            resultado = db_cur.fetchall()
            print('from db user_id: ' ,resultado[0][0])
            db_cur.close()
            # Return connection back to pool
            db_pool.putconn(db_conn)
            print('connection returned to pool')
            return resultado[0][0]

    except (Exception, pg.DatabaseError) as error:
        print('user_by_id PGDB conection error: ', error)
        return False
    return False


class User():
    def __init__(self, id, username, email, rol, options, enabled):
        self.id       = id
        self.username = username
        self.email    = email
        self.rol      = rol
        self.options  = options
        self.enabled  = enabled
    
    # UserMixin 
    @property
    def is_active(self):
        #return True
        return self.enabled

    #@property
   # def is_authenticated(self):
   #     return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            #return text_type(self.id)
            return self.id
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    def __eq__(self, other):
        '''
        Checks the equality of two `UserMixin` objects using `get_id`.
        '''
        if isinstance(other, UserMixin):
            return self.get_id() == other.get_id()
        return NotImplemented

    def __ne__(self, other):
        '''
        Checks the inequality of two `UserMixin` objects using `get_id`.
        '''
        equal = self.__eq__(other)
        if equal is NotImplemented:
            return NotImplemented
        return not equal



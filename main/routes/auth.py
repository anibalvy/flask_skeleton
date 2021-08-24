import flask
from main import app, login_required
from main.forms.auth import FormLogin
import main.models.auth as auth

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    # initializing login data 
    login_form = FormLogin() 
    if login_form.validate_on_submit(): 
        print('Validatin login from post on user '+ login_form.username.data) 
        username = login_form.username.data 
        password = login_form.password.data 
        user_data = auth.user_validation(username, password) 
        print('user validated: ',user_data)
        if user_data['error']:
            flask.flash('Error: '+ user_data['error'])
        else:
            if user_data['enabled']:
                if user_data['valid']: 
                    flask.session['id'] = user_data['id']
                    flask.session['username'] = user_data['username']
                    flask.session['email'] = user_data['email']
                    flask.session['rol'] = user_data['rol']
                    flask.session['options'] = user_data['options']
                    flask.session['enabled'] = user_data['enabled'] 
                    current_user = auth.User(user_data['id'], user_data['username'], user_data['email'], user_data['rol'], user_data['options'], user_data['enabled'] )
                    return flask.redirect(flask.url_for('dashboard') ) 
                else: 
                    flask.flash(f'Credenciales invalidas', category='danger')
            else: 
                flask.flash('Cuenta deshabilitada') 
    print(login_form.errors)
    if login_form.errors != {}: #If there are not errors from the validations         
        for err_msg in login_form.errors.values():                                    
            flask.flash(f'There was an error with validation of user: {err_msg}', category='danger')
    return flask.render_template('login.html', login_form=login_form, this_page='login')


@app.route('/logout')
def logout():
  flask.session.pop('id', None)
  flask.session.pop('username', None)
  flask.session.pop('email', None)
  flask.session.pop('rol', None)
  flask.session.pop('options', None)
  flask.session.pop('enabled', None)
  flask.flash('You have been signed out.')
  #print('Login out: ',flask_login.current_user)
  #flask_login.logout_user()
  #print('Login out already: ',flask_login.current_user)
  return flask.redirect(flask.url_for('login'))        
    

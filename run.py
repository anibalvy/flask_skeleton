import os
from main import app
from flask_sslify import SSLify
print(f"__file__ : {__file__}")
context = ('web.crt', 'web.key')
sslify = SSLify(app)

if __name__ == '__main__':
    #app.run(debug=True)
    #app.run(os.getenv('DEBUG'))
    #app.run(debug=os.getenv('DEBUG'), host='0.0.0.0', port=5000)
    #app.run(debug=True, host='0.0.0.0', port=5000)

    context = ('web.crt', 'web.key')
    app.run(debug=os.getenv('DEBUG'), host='0.0.0.0', port=5000, ssl_context=context)
    #app.run(debug=os.getenv('DEBUG'), host='0.0.0.0', port=5000, ssl_context='adhoc')
    

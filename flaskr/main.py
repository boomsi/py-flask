from flask import Flask, url_for, request, render_template, make_response, abort
from markupsafe import escape
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route("/")
def index():
    return "Index Page"


@app.get('/login')
def get_login():
    return get_the_login()

@app.post('/login')
def post_login():
    return post_the_login()

def post_the_login():
    username = request.form['username']
    pwd = request.form['password']
    print(username, pwd)
    return 'do the login'

def get_the_login():
    next = request.args.get('next')
    print(next)
    res = make_response(render_template('login.html'))
    res.set_cookie('next', next)
    # abort(401)
    res.headers.add('abc', 'def')
    app.logger.debug('A value for debugging')
    return res

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

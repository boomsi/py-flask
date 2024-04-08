from flask import jsonify
from flaskr import create_app
from flaskr.utils.error import InvalidAPIUsage
from flaskr.routes import auth, blog

app = create_app()

app.register_blueprint(auth.bp)
app.register_blueprint(blog.bp)
app.add_url_rule('/', endpoint='index')


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(e):
    return jsonify(e.to_dict()), e.status_code

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e), code = 100), 404

@app.route('/error')
def error():
    raise InvalidAPIUsage('Page not found')


@app.route('/abc')
def abc():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(port=5002, debug=True)

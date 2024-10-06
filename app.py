from flask import Flask, render_template, abort

app = Flask(__name__)

from werkzeug.middleware.proxy_fix import ProxyFix

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route("/")
def home():
    return render_template('homepage.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/planet/<int:planet_id>")
def planet(planet_id):
    if planet_id < 1 or planet_id > 4:
        abort(404)
    else:
        return render_template(f'Planet{str(planet_id)}.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
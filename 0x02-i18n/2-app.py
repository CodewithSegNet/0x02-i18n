#!/usr/bin/env python3
""" get_locale function use to determine the \
        best match """
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ represents a flask babel configuration """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def index():
    return render_template('2-index.html')


@babel.localeselector
def get_locale() -> str:
    return request.accept_languages.best_match(app.config['LANGUAGE'])


app.run(host="0.0.0.0", port=5000)

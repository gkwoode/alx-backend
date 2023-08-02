#!/usr/bin/env python3
"""Basic Babel setup"""

from flask import Flask
from flask import render_template
from flask import request
from flask_babel import Babel
from flask_babel import gettext as _

app = Flask(__name__)
babel = Babel(app)


# Create a Config class with available languages
class Config:
    """Babel config"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Set Babel's default locale and timezone using Config class
app.config.from_object(Config)
babel.init_app(app)


@babel.localeselector
def get_locale():
    """Get locale from request"""

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Function"""

    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)

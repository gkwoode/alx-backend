#!/usr/bin/env python3
"""Force locale with URL parameter"""

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

    requested_locale = request.args.get('locale')

    if requested_locale and requested_locale in app.config['LANGUAGES']:
        # Return if requested locale is supported
        return requested_locale

    # If requested locale is supported then return to the previous behaviour
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    """Function"""

    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)

#!/usr/bin/env python3
"""Infer appropriate time zone"""

from flask import Flask
from flask import render_template
from flask import request
from flask import g
from flask_babel import Babel
from flask_babel import gettext as _

app = Flask(__name__)
babel = Babel(app)


# User table in database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    # return request.accept_languages.best_match(app.config['LANGUAGES'])

    # Check if user is logged in with a preferred locale
    user_locale = g.user.get('locale') if g.user else None
    if user_locale and user_locale in app.config['LANGUAGES']:
        return user_locale

    header_locale = (
            request.accept_languages.best_match(app.config['LANGUAGES'])
            )
    if header_locale:
        return header_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])

    # Return to default locale if condition not true
    return app.config['BABEL_DEFAULT_LOCALE']


def get_user():
    """Function for login"""

    user_id = request.args.get('login_as')

    if user_id and int(user_id) in users:
        return users[int(user_id)]

    return None


@app.before_request
def before_request():
    """Function to call get_user() to find users"""

    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    """Function for time using babel.timezoneselector"""

    # Find timezone parameter in URL parameters
    requested_timezone = request.args.get('timezone')
    if requested_timezone:
        try:
            pytz.timezone(requested_timezone)
            return requested_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Find time zone from user settings
    user_timezone = g.user.get('timezone') if g.user else None
    if user_timezone:
        try:
            pytz.timezone(user_timezone)
            return user_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return 'UTC'


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    """Function"""

    user_timezone = pytz.timezone(get_timezone())
    current_time = datetime.datetime.now(user_timezone)
    formatted_time = format_datetime(
        current_time,
        format='medium',
        locale=get_locale()
    )

    if get_locale() == 'fr':
        current_time_msg = _(
            "Nous sommes le %(current_time)s.",
            current_time=formatted_time
        )
    else:
        current_time_msg = _(
            "The current time is %(current_time)s.",
            current_time=formatted_time
        )

    return render_template('index.html', current_time_msg=current_time_msg)


if __name__ == '__main__':
    app.run(debug=True)

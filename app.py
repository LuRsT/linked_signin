from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from linkedin_auth import get_access_token
from linkedin_auth import get_authorization_url
from linkedin_get_profile import get_profile_info_from_linkedin


APP = Flask(__name__)


@APP.route("/")
def index():
    return "<a href='{}'>Linkedin Login</a>".format(get_authorization_url())


@APP.route("/login")
def login():
    code = request.args.get('code')
    access_token = get_access_token(code)
    return redirect(url_for('profile_info', access_token=access_token))


@APP.route("/profile/<string:access_token>")
def profile_info(access_token):
    profile_info = get_profile_info_from_linkedin(access_token)
    return render_template('profile_info.html', profile_info=profile_info)


if __name__ == "__main__":
    APP.run(port=8000, debug=True)

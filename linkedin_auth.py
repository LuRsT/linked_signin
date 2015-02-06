from os import environ
from webbrowser import open as browser_open

from linkedin import linkedin

CONSUMER_KEY = environ.get('CONSUMER_KEY')
CONSUMER_SECRET = environ.get('CONSUMER_SECRET')

RETURN_URL = 'http://localhost:8000/login'


def _get_authentication():
    authentication = linkedin.LinkedInAuthentication(
        CONSUMER_KEY,
        CONSUMER_SECRET,
        RETURN_URL,
        linkedin.PERMISSIONS.enums.values(),
    )
    return authentication


def get_authentication_url():
    authentication = _get_authentication()
    return authentication.authorization_url


def get_access_token(code):
    authentication = _get_authentication()
    authentication.authorization_code = code
    return authentication.get_access_token().access_token


if __name__ == "__main__":
    authorization_url = get_authentication_url()
    print 'Opening {} in your browser...'.format(authorization_url)
    browser_open(authorization_url, new=0, autoraise=True)

    code = input('Enter code (from redirected URL): ')
    print get_access_token(code)

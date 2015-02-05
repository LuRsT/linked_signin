from json import dumps as to_json
from os import environ

from linkedin import linkedin


DEFAULT_FIELDS = (
    'first-name',
    'last-name',
    'location',
    'industry',
    'picture-url',
    'email-address',
    'positions',
    'headline',
)


def get_profile_info_from_linkedin(access_token, fields=DEFAULT_FIELDS):
    application = linkedin.LinkedInApplication(token=access_token)
    profile_info = application.get_profile(selectors=fields)
    return profile_info


if __name__ == "__main__":
    token = environ.get('ACCESS_TOKEN')
    print to_json(get_profile_info_from_linkedin(token))

# Linkedin Sign-in Playground

This is a simple flask app that shows how linkedin authentication and
`get_profile` endpoint works.

This was made for educational purpuses, DO NOT use this in production,
I know it looks good, but this wasn't made with that in mind.

## How to use this?

### How to install

#### Pre-requisites

- You need a Linkedin account in order to:
- Create an app in order to:
- Get `CONSUMER_KEY` and the `CONSUMER_SECRET`
- NOTE: As the return url for oauth, this app expects it to be
`http://localhost:8000/login`

Once you have that:

    $ git clone # this repo
    $ mkvirtualenv linkedin_signin
    $ pip install -r requirements.txt

Then pick your poison.

### In the browser (Recommended)

    # Make sure you have all the environment variables you need:
    # CONSUMER_KEY, CONSUMER_SECRET

    $ python app.py

    # Open your browser http://localhost:8000 and follow the steps :)

### In the console

    # Make sure you have all the environment variables you need:
    # CONSUMER_KEY, CONSUMER_SECRET

    $ python linkedin_auth.py

    # This will open your browser with a page so you can input your linkedin
    # credentials, after that you will be redirected to a url that hopefully
    # returns a 404, copy the value of the GET parameter "code" and paste in
    # the console (the script will prompt you for it).
    # After that, an access_token will be spit out, copy that and use it as
    # the environment variable ACCESS_TOKEN and run the next script:

    $ python linkedin_get_profile

Note: The output will be in json, so feel free to use a tool to pretty print it.

## Recommended documentation:

- [Linkedin Profile Fields](https://developer.linkedin.com/documents/profile-fields)
- [In case you don't know Flask](http://flask.pocoo.org/docs/0.10/)

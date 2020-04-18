from flask import Flask, request, jsonify
from datetime import timedelta
from validators import url
import string
import secrets
import redis

# TODO: validate the input urls, write a function to reload the stored dict of
# tokens and urls.

host = "localhost:5000/"
rc = redis.Redis()
strict_redis = redis.StrictRedis()

html_form = """
<!DOCTYPE html>
<html>
<body>

<h2>HTML Forms</h2>

<form action="/shorten" method="post">
  <label for="url">URL:</label><br>
  <input type="text" id="url" name="url" value="girishjoshi.io"><br>
  <input type="submit" value="Submit">
</form>

</body>
</html>
"""

config = {"urls-file": "urls.txt"}
app = Flask(__name__)

tokens = {}


def set_token(url, short_ver):
    """
    dumps the urls along with the tokens to a file.
    """
    strict_redis.setex(short_ver, timedelta(days=1), value=url)


@app.route("/")
def index():
    return html_form


@app.route("/<token>")
def retrive(token):
    """
    retrives the url from redis.
    """
    orig_url = strict_redis.get(token)
    if token:
        orig_url = orig_url.decode("utf-8")
        return f"""<!DOCTYPE html>
        <meta http-equiv="refresh" content="0;{orig_url}">
        <html>
        </html> """
    return "not found"


@app.route("/shorten", methods=["GET", "POST"])
def shorten():
    try:
        if request.method == "POST":
            print("need to process")
            if "url" in request.form:
                # TODO: validate the url
                print(request.form["url"])
                input_url = request.form["url"]
                if not url(input_url):
                    input_url = "http://" + input_url
                token = secrets.token_urlsafe(6)
                tokens[token] = input_url
                set_token(input_url, token)
                return f"""{input_url}: <a
            href='/{token}'>{host}{token}</a>"""
            else:
                return "url not provided"

        # TODO: implement the same for get requests.
        return "not processing the request"
    except Exception as e:
        return "some thing went wrong" + str(e)


if __name__ == "__main__":
    app.run()

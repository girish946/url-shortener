from flask import Flask, request, jsonify
import string
import secrets

# TODO: validate the input urls, write a function to reload the stored dict of
# tokens and urls.

html_form = """
<!DOCTYPE html>
<html>
<body>

<h2>HTML Forms</h2>

<form action="/shorten" method="post">
  <label for="url">URL:</label><br>
  <input type="text" id="url" name="url" value="something.com"><br>
  <input type="submit" value="Submit">
</form>

</body>
</html>
"""

config = {"urls-file": "urls.txt"}
app = Flask(__name__)

tokens = {}

def dump_new_url(url, short_ver):
    """
    dumps the urls along with the tokens to a file.
    """
    with open(config["urls-file"], "a") as uf:
        uf.write(short_ver+":"+url+"\n")


@app.route("/")
def index():
    return html_form

@app.route("/get/<token>")
def retrive(token):
    """
    retrives the url from tokens dict.
    """
    if(token in tokens):
        return tokens[token]
    return "not found"

@app.route("/shorten", methods=["GET", "POST"])
def shorten():
    try:
        if request.method == "POST":
            print("need to process")
            if("url" in request.form):
                # TODO: validate the url
                print(request.form["url"])
                url = request.form["url"]
                token = secrets.token_urlsafe(6)
                tokens[token] = url
                dump_new_url(url, token)

                return jsonify({url: "localhost:5000/get/"+token})
            else:
                return "url not provided"

        # TODO: implement the same for get requests.
        return "not processing the request"
    except Exception as e:
        return "some thing went wrong"+ str(e)

if __name__ == "__main__":
    app.run()

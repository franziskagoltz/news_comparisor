"""server file for news comparison app"""

import os
from flask import Flask, render_template, redirect, request, jsonify
from jinja2 import StrictUndefined
import news_api

app = Flask(__name__)

# For usage of flask session and debug toolbar
app.secret_key = "IN_DEV"

# StrictUndefinded raises errors for undefined variables, otherwise jinja
# does not give us an error, but fails silently
app.jinja_env.undefined = StrictUndefined

# auto-reloads changes we made, so we don't have to reload manually everytime
# we make a little change
app.jinja_env.auto_reload = True


news_api_key = os.environ.get("news_api_key")


@app.route("/")
def index():
    """render index page"""

    return render_template("index.html")


@app.route("/get-news.json")
def get_news():
    """make api call and return data for wordcloud"""

    cnn = news_api.cnn(news_api_key)

    cnn_words = news_api.count_words(cnn)

    return jsonify({"cnn": cnn_words})


if __name__ == "__main__":
    # Setting debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    app.run(host="0.0.0.0")
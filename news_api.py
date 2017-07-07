"""api calls to news api for cnn, breitbart, new york times"""


import requests


def cnn(api_key):
    """make api call for cnn, return body of text with top news"""

    cnn = requests.get("https://newsapi.org/v1/articles?source=cnn&"+
                       "sortBy=top&apiKey="+api_key)

    cnn_articles = cnn.json()["articles"]

    cnn_text = ""

    for article in cnn_articles:

        if article["title"]:
            cnn_text += article["title"] + " "
        if article["description"]:
            cnn_text += article["description"] + " "

    return cnn_text


def count_words(str):
    """create dictionary with word and occurrence"""

    word_count = {}

    ignore = {"as", "in", "the", "on", "a", "at", "is", "and", "of", "there",
              "to"}

    for word in str.split():

        if word.lower() not in ignore:
            word_count[word] = word_count.get(word, 0)
            word_count[word] += 1

    return word_count

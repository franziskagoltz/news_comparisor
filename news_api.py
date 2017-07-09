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

    return count_words(cnn_text)


def nyt(api_key):
    """make api call for new york times, return body of text with top news"""

    nyt = requests.get("https://newsapi.org/v1/articles?source=the-new-york-times"+
                       "&sortBy=top&apiKey="+api_key)

    nyt_articles = nyt.json()["articles"]

    nyt_text = ""

    for article in nyt_articles:

        if article["title"]:
            nyt_text += article["title"] + " "
        if article["description"]:
            nyt_text += article["description"] + " "

    return count_words(nyt_text)


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

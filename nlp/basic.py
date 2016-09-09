# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from textblob import TextBlob


def get_search_domain():
    return ['aaa', 'aniruddha']


def get_targeted_sentiment(text):
    blob = TextBlob(text)
    sentiments = dict()
    search_domain = get_search_domain()

    for sentence in blob.sentences:
        nouns = [tagged[0] for tagged in sentence.pos_tags
                 if tagged[1].startswith('NN')]
        sentiment = sentence.sentiment

        for noun in nouns:
            if noun in search_domain:
                if noun not in sentiments.keys():
                    sentiments[noun] = dict()
                    sentiments[noun]['polarity'] = 0.0
                    sentiments[noun]['count'] = 0
                sentiments[noun]['polarity'] += sentiment.polarity
                sentiments[noun]['count'] += 1

    return sentiments

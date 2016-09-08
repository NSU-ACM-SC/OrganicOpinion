# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import requests

import cPickle as pickle

NSU_CSE = '192402057456517'


def get_next(fb_dict):
    if fb_dict.get('paging') and fb_dict.get('paging').get('next'):
        return requests.get(fb_dict.get('paging').get('next')).json()


def load_posts(id_, graph, count=1):
    posts = list()
    for page in xrange(count):
        if page == 0:
            group_posts = graph.get_connections(id=id_, connection_name='feed')
        else:
            group_posts = get_next(group_posts)
        for post in group_posts.get('data'):
            posts.append(post.get('message'))
    return posts


def load_comments(id_, graph, count=1):
    comments = []
    for page in xrange(count):
        if page == 0:
            post_comments = graph.get_connections(id=id_,
                                                  connection_name='comment')
        else:
            post_comments = get_next(post_comments)
        for post in post_comments.get('data'):
            comments.append(post.get('message'))
    return comments

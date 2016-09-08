# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import argparse
import facebook

from social.fb_connector import load_posts, load_comments, NSU_CSE
from utils.exim import save_socialdata_as_list


def main():

    # parse from command_line
    parser = argparse.ArgumentParser()
    parser.add_argument("access_token", help="Facebook access token")
    args = parser.parse_args()

    # connect with FB API
    graph = facebook.GraphAPI(access_token=args.access_token, version='2.7')
    posts = load_posts(NSU_CSE, graph, 1)
    comments = []
    for post in posts:
        for comment in load_comments(post.get('id'), graph):
            comments.append(comment.get('message'))
    save_socialdata_as_list(social_data=comments, fieldname='comment', filepath='test.csv')

if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import argparse
import facebook

NSU_CSE = '192402057456517'


def main():

    # parse from command_line
    parser = argparse.ArgumentParser()
    parser.add_argument("access_token", help="Facebook access token")
    args = parser.parse_args()

    # connect with FB API
    graph = facebook.GraphAPI(access_token=args.access_token, version='2.7')
    group_posts = graph.get_connections(id=NSU_CSE, connection_name='feed')
    load_posts(group_posts, graph)


def load_posts(posts, graph):
    for post in posts.get('data'):
        comments = graph.get_connections(id=post.get('id'),
                                         connection_name='comments')
        for comment in comments.get('data'):
            if 'good' in comment.get('message').lower():
                print(comment.get('message'))


if __name__ == '__main__':
    main()

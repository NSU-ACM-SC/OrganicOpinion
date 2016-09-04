# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import argparse
import facebook

if __name__ == '__main__':
    NSU_CSE = '192402057456517'

    # parse from command_line
    parser = argparse.ArgumentParser()
    parser.add_argument("access_token", help="Facebook access token")
    args = parser.parse_args()

    # connect with FB API
    graph = facebook.GraphAPI(access_token=args.access_token, version='2.7')
    group_posts = graph.get_connections(id=NSU_CSE, connection_name='feed')
    group_posts = [post.get('message') for post in group_posts.get('data')]

    for post in group_posts:
        print(post)

    # print(group_posts)

# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import argparse
import facebook

from fb_connector import load_posts, load_comments, NSU_CSE


def main():

    # parse from command_line
    parser = argparse.ArgumentParser()
    parser.add_argument("access_token", help="Facebook access token")
    args = parser.parse_args()

    # connect with FB API
    graph = facebook.GraphAPI(access_token=args.access_token, version='2.7')

if __name__ == '__main__':
    main()

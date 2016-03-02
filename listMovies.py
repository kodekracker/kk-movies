#! /usr/bin/env python
# -*- coding: utf-8 -*-


#==================================================================
# Set MOVIES_FOLDER_PATH environment variable in your
# .bashrc file located in root of home directory
# NOTE :: write this in .bashrc file in the end of file
#
# export MOVIES_FOLDER_PATH="path-to-movies-root-folder"
#
# =================================================================

import os
import traceback
import pprint
import datetime
import codecs

from jinja2 import FileSystemLoader
from jinja2 import Environment

def datetimeformat(value, format='%I:%M %p , %d-%m-%Y'):
    return value.strftime(format)

def create_output_dir_if_not_exists():
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    print curr_dir
    if not os.path.exists(curr_dir+"/content"):
        os.makedirs(curr_dir+"/content")

def createHtml(movies_listing):
    '''
    To create index HTML page
    '''
    env = Environment(loader=FileSystemLoader('templates'))
    env.filters['datetimeformat'] = datetimeformat
    template = env.get_template('index-template.html')
    output_template = template.render(movies_listing=movies_listing)

    with codecs.open("content/index.html", "w+", "utf-8") as fh:
        fh.write(output_template)

def createMarkdown(movies_listing):
    '''
    To create index Markdown page
    '''
    with codecs.open("content/index.md", "w+", "utf-8") as fh:
        for d in movies_listing:
            dirname = d["dirname"]
            movies = d["movies"]
            fh.write("#%s\n"%(dirname))
            for movie in movies:
                fh.write("%d. %s\n"%(movies.index(movie)+1, movie))
            fh.write("\n")

def main():
    # a output list of dicts in which each dict contains data of one
    # particular directory
    movies_listing = []
    try :
        # get environment variable value
        movies_path = os.getenv('MOVIES_FOLDER_PATH')

        # check if environment variable exists or not
        if os.path.exists(movies_path):

            # get list of all directories in root directory
            dirs = [d for d in os.listdir(movies_path) if \
            os.path.isdir(os.path.join(movies_path,d))]

            # iterate each directory to collect movies list
            for d in dirs:

                # collect all movies in particular directory
                movies = [o.decode('utf-8') for o in os.listdir(os.path.join(movies_path,d) \
                     ) if os.path.isdir(os.path.join(movies_path, d, o))]

                # sort the names of movies alphabetically
                movies.sort()

                # check if atleast one movie exist in directory
                if len(movies):
                    # append a dict contain a directory data
                    movies_listing.append({
                        "dirname" : str(d),
                        "updated_at" : datetime.datetime.now(),
                        "movies"  : movies
                        })

            # pprint.pprint(movies_listing)
            create_output_dir_if_not_exists()
            createMarkdown(movies_listing)
            createHtml(movies_listing)

        else:
            print "Error :: No MOVIES_FOLDER_PATH environment variable set."

    except:
        traceback.print_exc()
        print "Exception Occured, Something wrong happened."

if __name__ == '__main__':
    main()

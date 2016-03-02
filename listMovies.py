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
import shutil

from jinja2 import FileSystemLoader
from jinja2 import Environment

# Full absolute path of template directory
TEMPLATES_DIR = os.path.dirname(os.path.abspath(__file__)) + "/templates"

# Full absolute path of output directory
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/content"


def datetimeformat(value, format='%I:%M %p , %d-%m-%Y'):
    """
    A Jinja template filter to print date object in human
    readable date string
    Ex: datetime.datetime(2016, 3, 3, 0, 40, 40, 921159)
        ==> 12:40 AM , 03-03-2016
    """
    return value.strftime(format)


def clean_and_create_output_dir():
    """
    Deletes a output directory if exists, and then create a
    fresh output directory
    """
    shutil.rmtree(OUTPUT_DIR,  ignore_errors=True)
    os.makedirs(OUTPUT_DIR)


def createHtml(movies_listing):
    """
    Creates a index.html page with data
    """
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    env.filters['datetimeformat'] = datetimeformat
    template = env.get_template('index-template.html')
    output_template = template.render(movies_listing=movies_listing)

    with codecs.open(OUTPUT_DIR + "/index.html", "w+", "utf-8") as fh:
        fh.write(output_template)


def createMarkdown(movies_listing):
    """
    Creates a index.md page with data
    """
    with codecs.open(OUTPUT_DIR + "/index.md", "w+", "utf-8") as fh:
        for d in movies_listing:
            dirname = d["dirname"]
            movies = d["movies"]
            fh.write("#%s\n"%(dirname))
            for movie in movies:
                fh.write("%d. %s\n"%(movies.index(movie)+1, movie))
            fh.write("\n")


def copy(src, dest):
    """
    Copies both files or directories from source to destination
    """
    try:
        shutil.copytree(src, dest, ignore=shutil.ignore_patterns(
            '*.py', '*.sh'))
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        # i.e it's a file
        if e.errno == shutil.errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print src, dest
            print('Directory not copied. Error: %s' % e)


def copy_static_folder():
    """
    Copies a static folder to output directory
    """
    copy(TEMPLATES_DIR + "/static", OUTPUT_DIR+"/static")


def copy_CNAME_file():
    """
    Copies a CNAME file to output directory
    """
    copy(TEMPLATES_DIR + "/CNAME", OUTPUT_DIR)


def create_output(movies_listing):
    """
    Runs all actions required to create an output for deployment
    """
    # Create output directory
    clean_and_create_output_dir()

    # Create a markdown file
    createMarkdown(movies_listing)

    # Create a html file
    createHtml(movies_listing)

    # Copy static folder
    copy_static_folder()

    # Copy CNAME file
    copy_CNAME_file()


def main():
    # a output list of dicts in which each dict contains data of one
    # particular directory
    movies_listing = []
    try :
        # get environment variable value
        movies_path = os.environ.get("MOVIES_FOLDER_PATH", None)

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

            # create an output for deployment
            create_output(movies_listing)

        else:
            print "Error :: No MOVIES_FOLDER_PATH environment variable set."

    except:
        traceback.print_exc()
        print "Exception Occured, Something wrong happened."

if __name__ == '__main__':
    main()

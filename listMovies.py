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

def main():
    try :
        movies_path = os.getenv('MOVIES_FOLDER_PATH')
        if os.path.exists(movies_path):
            dirs = [d for d in os.listdir(movies_path) if \
            os.path.isdir(os.path.join(movies_path,d))]

            with open("content/index.md", "w") as f:
                for d in dirs:
                    movies = [o for o in os.listdir(os.path.join(movies_path,d)
                     ) if os.path.isdir(os.path.join(movies_path, d, o))]

                    if len(movies):
                        f.write("#%s\n"%(d))
                        for movie in movies:
                            f.write("%d. %s\n"%(movies.index(movie)+1, movie))
                        f.write("\n")
        else:
            print "Error :: No MOVIES_FOLDER_PATH environment variable set."

    except:
        traceback.print_exc()
        print "Exception Occured, Something wrong happened."

if __name__ == '__main__':
    main()

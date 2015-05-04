#!/bin/bash

#==================================================================
# Set MOVIES_FOLDER_PATH environment variable in your
# .bashrc file located in root of home directory
# NOTE :: write this in .bashrc file in the end of file
#
# export MOVIES_FOLDER_PATH=write-path-here
#
# =================================================================

CURRENT_PATH=$(pwd)
FILENAME="${CURRENT_PATH}/index.md"

if [ ! -d "$MOVIES_FOLDER_PATH" ]; then
    echo "Error :: No such $MOVIES_FOLDER_PATH directory does not exists"
    exit 1
fi

cd "$MOVIES_FOLDER_PATH"

if [  -d "English-1" ]; then
    tree -ai -L 1 English-1 > $FILENAME
    echo "" >> $FILENAME
    echo "English-1 directory processed"
fi

if [  -d "English-2" ]; then
    tree -ai -L 1 English-2 >> $FILENAME
    echo "" >> $FILENAME
    echo "English-2 directory processed"
fi

if [  -d "English-3" ]; then
    tree -ai -L 1 English-2 >> $FILENAME
    echo "" >> $FILENAME
    echo "English-3 directory processed"
fi

if [  -d "Series Addition" ]; then
    tree -ai -L 1 "Series Addition" >> $FILENAME
    echo "" >> $FILENAME
    echo "Series Addition directory processed"
fi

cd "$CURRENT_PATH"

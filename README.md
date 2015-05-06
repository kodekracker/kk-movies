# kk-movies
A movies listing which i have in my external Dell HDD.

## Instructions
1. Set MOVIES_FOLDER_PATH environment variable in your .bashrc file located in root of home directory

    ```shell
        export MOVIES_FOLDER_PATH="path-to-movies-root-folder"
    ```

2. Install python required packages

    ```shell
        $ pip install -r requirements.txt
    ```

3. To create new listing of movies

    ```shell
        $ invoke create
    ```

4. To push new changes to gh-pages branch
    ```shell
        $ invoke push
    ```

#! /usr/bin/env python
# -*- coding: utf-8 -*-

from invoke import task, run

@task
def create():
    run('python listMovies.py')

@task
def push():
    run('ghp-import -pm "(updated): updated index.html" content/')

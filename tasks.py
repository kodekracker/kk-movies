#! /usr/bin/env python
# -*- coding: utf-8 -*-

from invoke import task, run

@task
def create():
    run('python listMovies.py')

# enter DNS File
def enter_dns_file(DNS=None):
    with open('content/CNAME', 'w') as f:
        f.write(DNS)

@task
def push(dns='movies.akshayon.net'):
    if dns:
        enter_dns_file(dns)
    run('ghp-import -pm "(updated): updated index.html" content/')

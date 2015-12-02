cookiecutter-django-magic-content
=================================

A cookiecutter_ template for Django using django-magic-content

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Description
-----------

A basic version of of the Daniel Greenfeld's cookiecutter-django.

It'll create a working django project structure (like when you use the `startproject`)

It uses the django 1.7 and all the django-magic-content dependecies

Usage
------

First, get cookiecutter_ installed ::

Set up your virtualenv::

    $ cd <your-envs-folder>
    $ virtualenv  --no-site-packages mysite-env
    $ cd mysite-env
    $ source bin/activate
    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter  https://github.com/huogerac/cookiecutter-django-magic-content

You'll be prompted for some questions, answer them...

It prompts you for questions. Answer them::

    Cloning into 'cookiecutter-django'...

    project_name (default is "project_name")? mysite
    repo_name (default is "repo_name")? mysite
    author_name (default is "Your Name")? <your name>
    email (default is "Your email")? <your email>
    description (default is "A short description of the project.")? My awesome website
    year (default is "Current year")? 2015


TODO ::

    $ cd mysite/
    $ pip install -r requirements/local.txt
    $ python ./manage.py syncdb
    $ python ./manage.py migrate
    $ ...complete here



Dependencies
------------



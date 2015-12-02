cookiecutter-django-magic-content
=================================

A cookiecutter_ template for Django using django-magic-content

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Description
-----------

A basic version of of the Daniel Greenfeld's cookiecutter-django.

It'll create a working django project structure (like when you use the `startproject`)

It uses the django 1.7 and all the django-magic-content dependecies

Pre Requirements
----------------

- Virtualenv (create isolated environment) ::
    
    $ sudo apt-get install python-pip
    $ sudo pip install virtualenv

- Pillow (make possible crop images) ::

    $ sudo apt-get install python-dev python-setuptools
    $ sudo apt-get install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk
    $ sudo apt-get python-imaging

- NODE and NPM (install assets from bower)
    $ curl -sL https://deb.nodesource.com/setup | sudo bash -
    $ sudo apt-get install nodejs
    $ sudo npm install npm -g
    $ npm install -g bower


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


Setup ::

    $ cd mysite/
    $ pip install -r requirements/local.txt
    $ chmod +x manage.py
    $ ./manage.py syncdb
    $ ./manage.py migrate
    $ ./manage.py bower install
    $ ./manage.py generate_colors
    $ ./manage.py restore_site --backup-name=personal_website --site-id=1
    $ ./manage.py runserver


Finally you can access the localhost:8000 and browser over you new awesome website.
You can also login and go back to the localhost:8000 and modify any content, as soon add/change images...


Dependencies
------------

The django-magic-content uses as base architecture:

- Django
- django-floppyforms
- django-ckeditor
- django-image-cropping

Instead of having a monolitic app, django-magic-content is separated in:

- `django-multisites-utils <https://github.com/DjenieLabs/django-multisites-utils>`_ : deal with having more than 1 website over the same project

- `django-magicbackup <https://github.com/DjenieLabs/django-magicbackup>`_ : helps backup/restore contents

- `django-frontend-decouple <https://github.com/DjenieLabs/django-frontend-decouple>`_ : good practices over the django template side

- `django-magicthemes <https://github.com/DjenieLabs/django-magicthemes>`_ : deal with the template beauty (CSS)

- `django-magic-gallery <https://github.com/DjenieLabs/django-magic-gallery>`_ : deal with upload, crop images as soon as make an site image library 

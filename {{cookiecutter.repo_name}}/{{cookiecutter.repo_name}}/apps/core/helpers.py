# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

import importlib
import inspect

from django.conf import settings
from django import forms
from django.db import models

from magicemailtemplates.sender import MagicEmail


def links_auto_discover():
    apps = map(lambda i: '{0}.models'.format(i), settings.LOCAL_APPS)

    full_links_list = []

    for app in apps:
        app_models = importlib.import_module(app)

        for _, obj in inspect.getmembers(app_models):
            if inspect.isclass(obj) and issubclass(obj, models.Model):
                if getattr(obj, 'list_links', False):

                    for instance in obj.site_objects.all():
                        full_links_list.append(instance.get_absolute_url())

    return full_links_list


class LinkListForm(object):

    show_links_on_field = ''

    def __init__(self, *args, **kws):
        super(LinkListForm, self).__init__(*args, **kws)
        self.fields[self.show_links_on_field] =\
            forms.ChoiceField(choices=self.link_choices)

    @property
    def link_choices(self):
        links = links_auto_discover()
        options = [['#top', '#top'],
                   ['#intro', '#intro'],
                   ['#first-topic', '#first-topic'],
                   ['#second-topic', '#second-topic'],
                   ['#third-topic', '#third-topic'],
                   ['#fourth-topic', '#fourth-topic'],
                   ['#final', '#final']]

        for link in links:
            options.append([link, link])

        return options


def is_site_owner(request):
    """ method helper for contactuspage """
    if request.user.is_authenticated():
        if request.user.is_staff or request.user.is_superuser:
            return True
    return False


def send_email(message_type, data, subject, email_to, reply_to):
    """ method helper for contactuspage """
    sender = MagicEmail("{0}".format(settings.DEFAULT_FROM_EMAIL))
    sender.using_template(message_type, data) \
          .with_subject(subject) \
          .reply_to(reply_to) \
          .send_to(email_to)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from ckeditor.fields import RichTextField

from django.db import models
from django.utils.translation import ugettext_lazy as _

from multisitesutils.models import Preferences


class SitePreferences(Preferences):
    """ See behaviours.Preferences how to use it """
    title = models.CharField(
        _('Site Title'), max_length=64, default='', blank=True)
    name = models.CharField(
        _('Site Name'), max_length=64, default='', blank=True)
    footer_title = models.CharField(
        _('Footer Title'), max_length=128, default='', blank=True)
    footer_address = RichTextField(
        _('Address'), max_length=256, default='', blank=True)
    footer_extra = RichTextField(
        _('Extra Information'), max_length=128, default='', blank=True)

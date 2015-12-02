# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from django.utils.crypto import get_random_string


class Permalinkable(models.Model):
    slug = models.SlugField(default=get_random_string)

    class Meta:
        abstract = True

    def get_absolute_url(self):
        return reverse('%s:%s_detail' % (self._meta.app_label,
                                         self._meta.model_name),
                       args=(self.slug,))


class Authorable(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        abstract = True

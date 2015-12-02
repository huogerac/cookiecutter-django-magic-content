# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView

from .views import (ShowLandingPageView,
                    SitePreferencesUpdateView, )

urlpatterns = patterns('',  # noqa

    url(r'^$', ShowLandingPageView.as_view()),

    url(r'^home/$', ShowLandingPageView.as_view(),
       name='core.landingpage'),

    url(r'^builds/$', TemplateView.as_view(template_name="core/builds.html"),
       name='core.builds'),

    url(r'^glossary/$',
       TemplateView.as_view(template_name="core/glossary.html"),
       name='core.glossary'),

    url(r'^help/$',
       TemplateView.as_view(template_name="core/help.html"),
       name='core.help'),

    url(r'^sitesetup/preferences/update/(?P<pk>\d+)/$',
       SitePreferencesUpdateView.as_view(),
       name='core.site.preferences.update'),

    url(r'^login/$',
       RedirectView.as_view(url="/admin/"),
       name="url_login_auth"),

    url(r'^logout/$',
       RedirectView.as_view(url="/admin/logout/"),
       name="auth_logout"),

)

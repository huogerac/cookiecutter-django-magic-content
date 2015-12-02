# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse_lazy

from magiccontent.mixins import OwnerRequiredMixin
from magiccontentnavigation.models import MenuItem

from .models import SitePreferences
from .forms import SitePreferencesForm, GAPreferencesForm


def can_edit_pages(user):
    """
    Used by the djenie-flatpages to define who can add/update pages content
    """
    if not user.is_authenticated():
        return False

    site_owner = user.is_staff
    return site_owner


def is_the_site_owner(request):
    return can_edit_pages(request.user)


class ShowLandingPageView(TemplateView):
    template_name = "core/landingpage.html"

    def get_context_data(self, **kwargs):
        context = super(ShowLandingPageView, self).get_context_data(**kwargs)
        # TODO: Should be better having a MIXIN for this...
        context['page_url'] = '/home'
        context['can_edit'] = can_edit_pages(self.request.user)
        context['topmenu_widget'] = MenuItem().current_menu.widget
        return context


class SitePreferencesUpdateView(OwnerRequiredMixin, UpdateView):
    model = SitePreferences
    form_class = SitePreferencesForm
    success_url = reverse_lazy('magiccontent.windows_close')

import re

from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site

import floppyforms.__future__ as forms

from floppyforms.widgets import TextInput
from googleanalytics.models import GoogleAnalyticsPreferences

from .models import SitePreferences


class CreateNewSiteForm(forms.Form):

    """  """
    site_name = forms.CharField(widget=TextInput(
        attrs={'placeholder': 'subdomain name'}), label=_("Sub Domain Name"))

    def clean(self):
        site_name = self.cleaned_data['site_name']
        site_name = "".join(site_name.lower().split())
        if len(site_name) <= 3:
            raise forms.ValidationError(
                _("This domain is invalid. It must be at least 3 chars long."))

        pattern = r'[^\.a-z0-9]'
        if re.search(pattern, site_name):
            raise forms.ValidationError(_("This domain is invalid."))

        existing_site = Site.objects.filter(
            domain__startswith='%s.' % site_name)
        if existing_site:
            raise forms.ValidationError(
                _("This domain is already in use. Please, inform a new one."))

        self.cleaned_data['site_name'] = site_name
        return self.cleaned_data

AREAS_DEFAULT = 'Welcome\nNews\nEvents\nMembers\nCampaigns\nAbout Us'


class SitePreferencesForm(forms.ModelForm):

    class Meta:
        model = SitePreferences
        fields = ('title', 'name', 'footer_title',
                  'footer_address', 'footer_extra',)


class GAPreferencesForm(forms.ModelForm):

    class Meta:
        model = GoogleAnalyticsPreferences
        fields = ('tracking_id',)

    def clean_tracking_id(self):
        tracking_id = self.cleaned_data.get('tracking_id', '')
        pattern = re.search(r'^(UA|YT|MO)-\d+-\d+', tracking_id)
        if not pattern:
            raise forms.ValidationError(
                'Your tracking id is not valid, please, try again')

        return tracking_id

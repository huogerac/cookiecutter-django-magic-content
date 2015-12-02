# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SitePreferences.name'
        db.add_column(u'core_sitepreferences', 'name',
                      self.gf('django.db.models.fields.CharField')(default=u'', max_length=64, blank=True),
                      keep_default=False)

        # Adding field 'SitePreferences.footer_title'
        db.add_column(u'core_sitepreferences', 'footer_title',
                      self.gf('django.db.models.fields.CharField')(default=u'', max_length=128, blank=True),
                      keep_default=False)

        # Adding field 'SitePreferences.footer_address'
        db.add_column(u'core_sitepreferences', 'footer_address',
                      self.gf('django.db.models.fields.TextField')(default=u'', max_length=256, blank=True),
                      keep_default=False)

        # Adding field 'SitePreferences.footer_extra'
        db.add_column(u'core_sitepreferences', 'footer_extra',
                      self.gf('django.db.models.fields.TextField')(default=u'', max_length=128, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SitePreferences.name'
        db.delete_column(u'core_sitepreferences', 'name')

        # Deleting field 'SitePreferences.footer_title'
        db.delete_column(u'core_sitepreferences', 'footer_title')

        # Deleting field 'SitePreferences.footer_address'
        db.delete_column(u'core_sitepreferences', 'footer_address')

        # Deleting field 'SitePreferences.footer_extra'
        db.delete_column(u'core_sitepreferences', 'footer_extra')


    models = {
        u'core.sitepreferences': {
            'Meta': {'object_name': 'SitePreferences'},
            'footer_address': ('django.db.models.fields.TextField', [], {'default': "u''", 'max_length': '256', 'blank': 'True'}),
            'footer_extra': ('django.db.models.fields.TextField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'footer_title': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['core']
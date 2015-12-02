# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'SitePreferences.footer_address'
        db.alter_column(u'core_sitepreferences', 'footer_address', self.gf('ckeditor.fields.RichTextField')(max_length=256))

        # Changing field 'SitePreferences.footer_extra'
        db.alter_column(u'core_sitepreferences', 'footer_extra', self.gf('ckeditor.fields.RichTextField')(max_length=128))

    def backwards(self, orm):

        # Changing field 'SitePreferences.footer_address'
        db.alter_column(u'core_sitepreferences', 'footer_address', self.gf('django.db.models.fields.TextField')(max_length=256))

        # Changing field 'SitePreferences.footer_extra'
        db.alter_column(u'core_sitepreferences', 'footer_extra', self.gf('django.db.models.fields.TextField')(max_length=128))

    models = {
        u'core.sitepreferences': {
            'Meta': {'object_name': 'SitePreferences'},
            'footer_address': ('ckeditor.fields.RichTextField', [], {'default': "u''", 'max_length': '256', 'blank': 'True'}),
            'footer_extra': ('ckeditor.fields.RichTextField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
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
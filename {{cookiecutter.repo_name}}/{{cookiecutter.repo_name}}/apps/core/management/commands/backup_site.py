# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from optparse import make_option

from fabric.colors import green

from django.core.management.base import BaseCommand

from magicbackup.helpers import MagicBackup


class Command(BaseCommand):
    help = 'Backup a Site'
    option_list = BaseCommand.option_list + (
        make_option('--backup-name', action='store', dest='backup_name',
                    type='string', help='A name for backup folder'),
        make_option('--site-id', action='store', dest='site_id',
                    type='int', help='The site ID'),
    )

    def handle(self, *args, **options):
        backup_name = options['backup_name']
        site_id = options['site_id']

        if not backup_name or not site_id:
            raise Exception('backup_name or site_id is missing')

        models = ["magiccontent.Widget",
                  "magiccontent.Area",
                  "magiccontent.SiteLink",
                  "magicgallery.Gallery",
                  "magicgallery.GalleryItem",
                  "textimagecontent.TextImageContent",
                  "formattedtextimagecontent.FormattedTextImageContent",
                  "iconcontent.IconContent",
                  "background.BackgroundArea",
                  "dividertextcontent.DividerTextContent",
                  "imagecontent.ImageContent",
                  "magiccontentnavigation.MenuItem",
                  "core.SitePreferences",
                  "magicthemes.ThemePreferences", ]

        backup = MagicBackup().site(site_id).save_as(backup_name)
        for model in models:
            print(green('backuping {0}...'.format(model)))
            backup.model(model).backup()

        print(green('new backup created at {0}'.format(backup.target_dir)))

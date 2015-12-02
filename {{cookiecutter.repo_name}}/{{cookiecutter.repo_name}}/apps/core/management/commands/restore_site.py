# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from optparse import make_option

from fabric.colors import green

from django.core.management.base import BaseCommand
from django.core.management import call_command

from magicbackup.helpers import MagicBackup


class Command(BaseCommand):
    help = 'Restore a Site'
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

        # IMPORTANT: if you update this list, please,
        #            see the site_creator.py module too
        models_list = ["magiccontent.Widget",
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

        restore = MagicBackup() \
            .from_backup(backup_name) \
            .to_site(site_id)

        for model in models_list:
            print(green('Restoring {0}...'.format(model)))
            restore.model(model).restore()

        print(green('site id {0} populated with backup {1}'.format(
            site_id, restore.original_path)))

        # generate new links
        # call_command('generate_site_links', site_id=site_id)

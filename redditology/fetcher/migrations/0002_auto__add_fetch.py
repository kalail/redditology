# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fetch'
        db.create_table(u'fetcher_fetch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('successful', self.gf('django.db.models.fields.NullBooleanField')(default=None, null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'fetcher', ['Fetch'])


    def backwards(self, orm):
        # Deleting model 'Fetch'
        db.delete_table(u'fetcher_fetch')


    models = {
        u'fetcher.fetch': {
            'Meta': {'object_name': 'Fetch'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'successful': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fetcher']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PostSnapshot'
        db.create_table(u'posts_postsnapshot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fetch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fetcher.Fetch'])),
            ('rank', self.gf('django.db.models.fields.IntegerField')()),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['posts.Post'])),
            ('num_comments', self.gf('django.db.models.fields.IntegerField')()),
            ('up_votes', self.gf('django.db.models.fields.IntegerField')()),
            ('down_votes', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'posts', ['PostSnapshot'])

        # Adding model 'Post'
        db.create_table(u'posts_post', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=32, primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('over_18', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('subreddit', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('created_on_reddit', self.gf('django.db.models.fields.DateTimeField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'posts', ['Post'])


    def backwards(self, orm):
        # Deleting model 'PostSnapshot'
        db.delete_table(u'posts_postsnapshot')

        # Deleting model 'Post'
        db.delete_table(u'posts_post')


    models = {
        u'fetcher.fetch': {
            'Meta': {'object_name': 'Fetch'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'successful': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'posts.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'created_on_reddit': ('django.db.models.fields.DateTimeField', [], {}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'over_18': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subreddit': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'posts.postsnapshot': {
            'Meta': {'object_name': 'PostSnapshot'},
            'down_votes': ('django.db.models.fields.IntegerField', [], {}),
            'fetch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fetcher.Fetch']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_comments': ('django.db.models.fields.IntegerField', [], {}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['posts.Post']"}),
            'rank': ('django.db.models.fields.IntegerField', [], {}),
            'up_votes': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['posts']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table('redditology_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('redditology', ['Author'])

        # Adding model 'Snapshot'
        db.create_table('redditology_snapshot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('redditology', ['Snapshot'])

        # Adding model 'Subreddit'
        db.create_table('redditology_subreddit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('redditology', ['Subreddit'])

        # Adding model 'Domain'
        db.create_table('redditology_domain', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('redditology', ['Domain'])

        # Adding model 'Post'
        db.create_table('redditology_post', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=32, primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('over_18', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('subreddit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['redditology.Subreddit'])),
            ('domain', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['redditology.Domain'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['redditology.Author'])),
            ('created_on_reddit', self.gf('django.db.models.fields.DateTimeField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('redditology', ['Post'])

        # Adding model 'PostSnapshot'
        db.create_table('redditology_postsnapshot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num_comments', self.gf('django.db.models.fields.IntegerField')()),
            ('snapshot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['redditology.Snapshot'])),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['redditology.Post'])),
            ('up_votes', self.gf('django.db.models.fields.IntegerField')()),
            ('down_votes', self.gf('django.db.models.fields.IntegerField')()),
            ('rank', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redditology', ['PostSnapshot'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table('redditology_author')

        # Deleting model 'Snapshot'
        db.delete_table('redditology_snapshot')

        # Deleting model 'Subreddit'
        db.delete_table('redditology_subreddit')

        # Deleting model 'Domain'
        db.delete_table('redditology_domain')

        # Deleting model 'Post'
        db.delete_table('redditology_post')

        # Deleting model 'PostSnapshot'
        db.delete_table('redditology_postsnapshot')


    models = {
        'redditology.author': {
            'Meta': {'object_name': 'Author'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        'redditology.domain': {
            'Meta': {'object_name': 'Domain'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        'redditology.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['redditology.Author']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_on_reddit': ('django.db.models.fields.DateTimeField', [], {}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['redditology.Domain']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'over_18': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subreddit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['redditology.Subreddit']"}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'redditology.postsnapshot': {
            'Meta': {'object_name': 'PostSnapshot'},
            'down_votes': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_comments': ('django.db.models.fields.IntegerField', [], {}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['redditology.Post']"}),
            'rank': ('django.db.models.fields.IntegerField', [], {}),
            'snapshot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['redditology.Snapshot']"}),
            'up_votes': ('django.db.models.fields.IntegerField', [], {})
        },
        'redditology.snapshot': {
            'Meta': {'object_name': 'Snapshot'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'redditology.subreddit': {
            'Meta': {'object_name': 'Subreddit'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['redditology']
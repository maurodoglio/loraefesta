# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Collection'
        db.create_table(u'loraweb_collection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=130)),
            ('name_it', self.gf('django.db.models.fields.CharField')(max_length=130, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=130, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=130)),
            ('title_it', self.gf('django.db.models.fields.CharField')(max_length=130, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=130, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('abstract', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('abstract_it', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('abstract_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('media', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('pub', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pub_order', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'loraweb', ['Collection'])

        # Adding model 'Yarn'
        db.create_table(u'loraweb_yarn', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['loraweb.Collection'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=130)),
            ('name_it', self.gf('django.db.models.fields.CharField')(max_length=130, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=130, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=130)),
            ('title_it', self.gf('django.db.models.fields.CharField')(max_length=130, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=130, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('abstract', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('abstract_it', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('abstract_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('text_it', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('text_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('media', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('pub', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pub_order', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'loraweb', ['Yarn'])

        # Adding model 'News'
        db.create_table(u'loraweb_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=130)),
            ('title_it', self.gf('django.db.models.fields.CharField')(max_length=130, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=130, null=True, blank=True)),
            ('abstract', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('abstract_it', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('abstract_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('text_it', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('text_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('media', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('pub', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pub_order', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'loraweb', ['News'])


    def backwards(self, orm):
        # Deleting model 'Collection'
        db.delete_table(u'loraweb_collection')

        # Deleting model 'Yarn'
        db.delete_table(u'loraweb_yarn')

        # Deleting model 'News'
        db.delete_table(u'loraweb_news')


    models = {
        u'loraweb.collection': {
            'Meta': {'object_name': 'Collection'},
            'abstract': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'abstract_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'abstract_it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '130'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'name_it': ('django.db.models.fields.CharField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'pub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pub_order': ('django.db.models.fields.SmallIntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '130'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'title_it': ('django.db.models.fields.CharField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'})
        },
        u'loraweb.news': {
            'Meta': {'object_name': 'News'},
            'abstract': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'abstract_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'abstract_it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pub_order': ('django.db.models.fields.SmallIntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_it': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '130'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'title_it': ('django.db.models.fields.CharField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'})
        },
        u'loraweb.yarn': {
            'Meta': {'object_name': 'Yarn'},
            'abstract': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'abstract_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'abstract_it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['loraweb.Collection']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '130'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'name_it': ('django.db.models.fields.CharField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'pub': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pub_order': ('django.db.models.fields.SmallIntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_it': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '130'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'}),
            'title_it': ('django.db.models.fields.CharField', [], {'max_length': '130', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['loraweb']
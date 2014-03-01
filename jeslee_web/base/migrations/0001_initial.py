# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ClothingSize'
        db.create_table(u'base_clothingsize', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'base', ['ClothingSize'])

        # Adding model 'Garment'
        db.create_table(u'base_garment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'base', ['Garment'])


    def backwards(self, orm):
        # Deleting model 'ClothingSize'
        db.delete_table(u'base_clothingsize')

        # Deleting model 'Garment'
        db.delete_table(u'base_garment')


    models = {
        u'base.clothingsize': {
            'Meta': {'object_name': 'ClothingSize'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'base.garment': {
            'Meta': {'object_name': 'Garment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['base']
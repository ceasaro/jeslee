# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OrderNumberGenerator'
        db.create_table(u'lfs_patch_ordernumbergenerator', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('last', self.gf('django.db.models.fields.IntegerField')(default=2014)),
            ('format', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal(u'lfs_patch', ['OrderNumberGenerator'])


    def backwards(self, orm):
        # Deleting model 'OrderNumberGenerator'
        db.delete_table(u'lfs_patch_ordernumbergenerator')


    models = {
        u'lfs_patch.ordernumbergenerator': {
            'Meta': {'object_name': 'OrderNumberGenerator'},
            'format': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'last': ('django.db.models.fields.IntegerField', [], {'default': '2014'})
        }
    }

    complete_apps = ['lfs_patch']
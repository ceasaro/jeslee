# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FashionRegistration'
        db.create_table(u'fashion_show_fashionregistration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('birth_date', self.gf('django.db.models.fields.DateField')(max_length=10)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('street_nr', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.CharField')(default='Netherlands', max_length=100)),
            ('fashion_show', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'fashion_show', ['FashionRegistration'])


    def backwards(self, orm):
        # Deleting model 'FashionRegistration'
        db.delete_table(u'fashion_show_fashionregistration')


    models = {
        u'fashion_show.fashionregistration': {
            'Meta': {'object_name': 'FashionRegistration'},
            'birth_date': ('django.db.models.fields.DateField', [], {'max_length': '10'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Netherlands'", 'max_length': '100'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fashion_show': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'street_nr': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['fashion_show']
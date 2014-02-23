# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FashionGarment'
        db.create_table(u'fashion_show_fashiongarment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('garment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Garment'])),
            ('size', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.ClothingSize'])),
        ))
        db.send_create_signal(u'fashion_show', ['FashionGarment'])

        # Adding model 'FashionModel'
        db.create_table(u'fashion_show_fashionmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('street_nr', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(default='Netherlands', max_length=100, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('size', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.ClothingSize'])),
        ))
        db.send_create_signal(u'fashion_show', ['FashionModel'])

        # Adding model 'FashionLocation'
        db.create_table(u'fashion_show_fashionlocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('street_nr', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(default='Netherlands', max_length=100, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'fashion_show', ['FashionLocation'])

        # Adding field 'FashionRegistration.age'
        db.add_column(u'fashion_show_fashionregistration', 'age',
                      self.gf('django.db.models.fields.CharField')(max_length=5, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'FashionGarment'
        db.delete_table(u'fashion_show_fashiongarment')

        # Deleting model 'FashionModel'
        db.delete_table(u'fashion_show_fashionmodel')

        # Deleting model 'FashionLocation'
        db.delete_table(u'fashion_show_fashionlocation')

        # Deleting field 'FashionRegistration.age'
        db.delete_column(u'fashion_show_fashionregistration', 'age')


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
        },
        u'fashion_show.fashiongarment': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'FashionGarment'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'garment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Garment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.ClothingSize']"})
        },
        u'fashion_show.fashionlocation': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'FashionLocation'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Netherlands'", 'max_length': '100', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'street_nr': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'fashion_show.fashionmodel': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'FashionModel'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Netherlands'", 'max_length': '100', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.ClothingSize']"}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'street_nr': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'fashion_show.fashionregistration': {
            'Meta': {'object_name': 'FashionRegistration'},
            'age': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'max_length': '10', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Netherlands'", 'max_length': '100', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fashion_show': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'street_nr': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['fashion_show']
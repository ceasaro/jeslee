# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'FashionRegistration.fashion_show' to match new field type.
        db.rename_column(u'fashion_show_fashionregistration', 'fashion_show', 'fashion_show_id')
        # Changing field 'FashionRegistration.fashion_show'
        db.alter_column(u'fashion_show_fashionregistration', 'fashion_show_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fashion_show.FashionShow'], null=True))
        # Adding index on 'FashionRegistration', fields ['fashion_show']
        db.create_index(u'fashion_show_fashionregistration', ['fashion_show_id'])


    def backwards(self, orm):
        # Removing index on 'FashionRegistration', fields ['fashion_show']
        db.delete_index(u'fashion_show_fashionregistration', ['fashion_show_id'])


        # User chose to not deal with backwards NULL issues for 'FashionRegistration.fashion_show'
        raise RuntimeError("Cannot reverse this migration. 'FashionRegistration.fashion_show' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Renaming column for 'FashionRegistration.fashion_show' to match new field type.
        db.rename_column(u'fashion_show_fashionregistration', 'fashion_show_id', 'fashion_show')
        # Changing field 'FashionRegistration.fashion_show'
        db.alter_column(u'fashion_show_fashionregistration', 'fashion_show', self.gf('django.db.models.fields.CharField')(max_length=100))

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
            'garment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'garment'", 'to': u"orm['base.Garment']"}),
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
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'street_nr': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'fashion_show.fashionmodel': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'FashionModel'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Netherlands'", 'max_length': '100', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'garment': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'model'", 'null': 'True', 'to': u"orm['fashion_show.FashionGarment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'model'", 'null': 'True', 'to': u"orm['base.ClothingSize']"}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'street_nr': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'fashion_show.fashionregistration': {
            'Meta': {'object_name': 'FashionRegistration'},
            'age': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Netherlands'", 'max_length': '100', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fashion_show': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fashion_show.FashionShow']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'remarks': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.ClothingSize']", 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'street_nr': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'fashion_show.fashionshow': {
            'Meta': {'ordering': "['start_time']", 'object_name': 'FashionShow'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'fashion_show'", 'to': u"orm['fashion_show.FashionLocation']"}),
            'models': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'fashion_shows'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['fashion_show.FashionModel']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'ticket_order_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fashion_show']
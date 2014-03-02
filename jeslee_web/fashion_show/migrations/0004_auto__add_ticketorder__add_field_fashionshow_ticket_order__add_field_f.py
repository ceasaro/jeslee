# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TicketOrder'
        db.create_table(u'fashion_show_ticketorder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('order_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'fashion_show', ['TicketOrder'])

        # Adding field 'FashionShow.ticket_order'
        db.add_column(u'fashion_show_fashionshow', 'ticket_order',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'fashion_show', null=True, to=orm['fashion_show.TicketOrder']),
                      keep_default=False)

        # Adding field 'FashionLocation.logo'
        db.add_column(u'fashion_show_fashionlocation', 'logo',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FashionLocation.website'
        db.add_column(u'fashion_show_fashionlocation', 'website',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'TicketOrder'
        db.delete_table(u'fashion_show_ticketorder')

        # Deleting field 'FashionShow.ticket_order'
        db.delete_column(u'fashion_show_fashionshow', 'ticket_order_id')

        # Deleting field 'FashionLocation.logo'
        db.delete_column(u'fashion_show_fashionlocation', 'logo')

        # Deleting field 'FashionLocation.website'
        db.delete_column(u'fashion_show_fashionlocation', 'website')


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
            'logo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'ticket_order': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'fashion_show'", 'null': 'True', 'to': u"orm['fashion_show.TicketOrder']"})
        },
        u'fashion_show.ticketorder': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'TicketOrder'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'order_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['fashion_show']
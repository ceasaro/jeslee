# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FashionShow'
        db.create_table(u'fashion_show_fashionshow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'fashion_show', to=orm['fashion_show.FashionLocation'])),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'fashion_show', ['FashionShow'])

        # Adding M2M table for field models on 'FashionShow'
        m2m_table_name = db.shorten_name(u'fashion_show_fashionshow_models')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fashionshow', models.ForeignKey(orm[u'fashion_show.fashionshow'], null=False)),
            ('fashionmodel', models.ForeignKey(orm[u'fashion_show.fashionmodel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['fashionshow_id', 'fashionmodel_id'])

        # Adding field 'FashionModel.garment'
        db.add_column(u'fashion_show_fashionmodel', 'garment',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'model', null=True, to=orm['fashion_show.FashionGarment']),
                      keep_default=False)


        # Changing field 'FashionModel.size'
        db.alter_column(u'fashion_show_fashionmodel', 'size_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['base.ClothingSize']))

    def backwards(self, orm):
        # Deleting model 'FashionShow'
        db.delete_table(u'fashion_show_fashionshow')

        # Removing M2M table for field models on 'FashionShow'
        db.delete_table(db.shorten_name(u'fashion_show_fashionshow_models'))

        # Deleting field 'FashionModel.garment'
        db.delete_column(u'fashion_show_fashionmodel', 'garment_id')


        # Changing field 'FashionModel.size'
        db.alter_column(u'fashion_show_fashionmodel', 'size_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['base.ClothingSize']))

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
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'FashionShow'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'fashion_show'", 'to': u"orm['fashion_show.FashionLocation']"}),
            'models': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'fashion_shows'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['fashion_show.FashionModel']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fashion_show']
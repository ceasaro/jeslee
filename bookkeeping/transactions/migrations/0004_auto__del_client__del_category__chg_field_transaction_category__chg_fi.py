# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Client'
        db.delete_table(u'transactions_client')

        # Deleting model 'Category'
        db.delete_table(u'transactions_category')


        # Changing field 'Transaction.category'
        db.alter_column(u'transactions_transaction', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Category']))

        # Changing field 'Transaction.client'
        db.alter_column(u'transactions_transaction', 'client_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Client']))

    def backwards(self, orm):
        # Adding model 'Client'
        db.create_table(u'transactions_client', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128, unique=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal(u'transactions', ['Client'])

        # Adding model 'Category'
        db.create_table(u'transactions_category', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal(u'transactions', ['Category'])


        # Changing field 'Transaction.category'
        db.alter_column(u'transactions_transaction', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['transactions.Category']))

        # Changing field 'Transaction.client'
        db.alter_column(u'transactions_transaction', 'client_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['transactions.Client']))

    models = {
        u'core.category': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Category'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'core.client': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Client'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Netherlands'", 'max_length': '100', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'street_nr': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'transactions.payment': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Payment', '_ormbases': [u'transactions.Transaction']},
            u'transaction_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['transactions.Transaction']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'transactions.receipt': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Receipt', '_ormbases': [u'transactions.Transaction']},
            u'transaction_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['transactions.Transaction']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'transactions.transaction': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Transaction'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'transactions'", 'null': 'True', 'to': u"orm['core.Category']"}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transactions'", 'to': u"orm['core.Client']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'pay_date': ('django.db.models.fields.DateField', [], {}),
            'tax_percentage': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['transactions']
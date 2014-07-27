# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Transaction.tax_percentage'
        db.add_column(u'transactions_transaction', 'tax_percentage',
                      self.gf('django.db.models.fields.IntegerField')(default=21),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Transaction.tax_percentage'
        db.delete_column(u'transactions_transaction', 'tax_percentage')


    models = {
        u'transactions.category': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Category'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'transactions.client': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Client'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
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
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'transactions'", 'null': 'True', 'to': u"orm['transactions.Category']"}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transactions'", 'to': u"orm['transactions.Client']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'pay_date': ('django.db.models.fields.DateField', [], {}),
            'tax_percentage': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['transactions']
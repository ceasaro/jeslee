# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Client'
        db.create_table(u'transactions_client', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'transactions', ['Client'])

        # Adding model 'Category'
        db.create_table(u'transactions_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'transactions', ['Category'])

        # Adding model 'Transaction'
        db.create_table(u'transactions_transaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('pay_date', self.gf('django.db.models.fields.DateField')()),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name='transactions', to=orm['transactions.Client'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='transactions', null=True, to=orm['transactions.Category'])),
        ))
        db.send_create_signal(u'transactions', ['Transaction'])

        # Adding model 'Payment'
        db.create_table(u'transactions_payment', (
            (u'transaction_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['transactions.Transaction'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'transactions', ['Payment'])

        # Adding model 'Receipt'
        db.create_table(u'transactions_receipt', (
            (u'transaction_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['transactions.Transaction'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'transactions', ['Receipt'])


    def backwards(self, orm):
        # Deleting model 'Client'
        db.delete_table(u'transactions_client')

        # Deleting model 'Category'
        db.delete_table(u'transactions_category')

        # Deleting model 'Transaction'
        db.delete_table(u'transactions_transaction')

        # Deleting model 'Payment'
        db.delete_table(u'transactions_payment')

        # Deleting model 'Receipt'
        db.delete_table(u'transactions_receipt')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
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
            'pay_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['transactions']
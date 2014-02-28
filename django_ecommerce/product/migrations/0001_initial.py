# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table('product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('sku', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal(u'product', ['Product'])

        # Adding model 'StoreProduct'
        db.create_table('store_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Store'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product.Product'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'product', ['StoreProduct'])

        # Adding model 'ProductAttribute'
        db.create_table('product_attribute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'product', ['ProductAttribute'])

        # Adding model 'ProductAttributeValue'
        db.create_table('product_attribute_value', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product.Product'])),
            ('attribute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product.ProductAttribute'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'product', ['ProductAttributeValue'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table('product')

        # Deleting model 'StoreProduct'
        db.delete_table('store_product')

        # Deleting model 'ProductAttribute'
        db.delete_table('product_attribute')

        # Deleting model 'ProductAttributeValue'
        db.delete_table('product_attribute_value')


    models = {
        u'core.store': {
            'Meta': {'object_name': 'Store', 'db_table': "'store'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sites.Site']", 'unique': 'True'})
        },
        u'product.product': {
            'Meta': {'object_name': 'Product', 'db_table': "'product'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'store': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Store']", 'through': u"orm['product.StoreProduct']", 'symmetrical': 'False'})
        },
        u'product.productattribute': {
            'Meta': {'object_name': 'ProductAttribute', 'db_table': "'product_attribute'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'product.productattributevalue': {
            'Meta': {'object_name': 'ProductAttributeValue', 'db_table': "'product_attribute_value'"},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.ProductAttribute']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.Product']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'product.storeproduct': {
            'Meta': {'object_name': 'StoreProduct', 'db_table': "'store_product'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.Product']"}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Store']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['product']
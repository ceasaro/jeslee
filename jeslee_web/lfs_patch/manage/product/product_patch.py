# from django.forms import forms, HiddenInput, ErrorList
from django.contrib.auth.decorators import permission_required
from django.views.decorators.http import require_POST
from lfs.manage.product.product import ProductDataForm, ProductStockForm, edit_product_data

from jeslee_web.lfs_patch import CheckboxIntegerInput

__author__ = 'ceasaro'

#
# We need to patch the ProductDataForm of lfs cause it uses a CheckboxInput widget, which cleans the data value
# to True or False, while lfs is expecting 1 or 0.
#
old_product_data_form__init__ = ProductDataForm.__init__


def new_product_data_form__init__(self, *args, **kwargs):
    old_product_data_form__init__(self, *args, **kwargs)
    self.fields["active_base_price"].widget = CheckboxIntegerInput()

ProductDataForm.__init__ = new_product_data_form__init__

#
# We need to patch the ProductStockForm of lfs cause it uses a CheckboxInput widget, which cleans the data value
# to True or False, while lfs is expecting 1 or 0.
#
old_product_stock_form__init__ = ProductStockForm.__init__


def new_product_stock_form__init__(self, *args, **kwargs):
    old_product_stock_form__init__(self, *args, **kwargs)
    if not kwargs.get("instance").is_variant():
        self.fields["active_packing_unit"].widget = CheckboxIntegerInput()

ProductStockForm.__init__ = new_product_stock_form__init__

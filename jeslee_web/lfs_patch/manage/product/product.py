from django import forms
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
# from django.forms import forms, HiddenInput, ErrorList
from django.forms.util import ErrorList
from django.forms.widgets import HiddenInput
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils import simplejson
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.http import require_POST
from lfs.caching.utils import lfs_get_object_or_404
from lfs.catalog.models import Product
from lfs.catalog.settings import VARIANT, PRODUCT_TEMPLATES
from lfs.core.utils import LazyEncoder
from lfs.manage.product.product import _get_filtered_products_for_product_view, VariantDataForm, lfs, \
    selectable_products_inline, ProductDataForm
from lfs.manufacturer.models import Manufacturer
from lfs.utils.widgets import SelectImage
from jeslee_web.lfs_patch import CheckboxIntegerInput

__author__ = 'ceasaro'

#
# We need to patch the ProductDataForm of lfs cause it uses a CheckboxInput widget, which cleans the data value
# to True or False, while lfs is expecting 1 or 0.
#
class ProductDataFormPatch(ProductDataForm):
    """
    Form to add and edit master data of a product.
    """
    def __init__(self, *args, **kwargs):
        super(ProductDataFormPatch, self).__init__(*args, **kwargs)
        self.fields["template"].widget = SelectImage(choices=PRODUCT_TEMPLATES)
        self.fields["active_base_price"].widget = CheckboxIntegerInput()
        man_count = Manufacturer.objects.count()
        if man_count > getattr(settings, 'LFS_SELECT_LIMIT', 20):
            self.fields["manufacturer"].widget = HiddenInput()

#
# patched the edit_product_data cause it's now used the ProductDataFormPatch form.
#
@permission_required("core.manage_shop", login_url="/login/")
@require_POST
def edit_product_data_patch(request, product_id, template_name="manage/product/data.html"):
    """Edits the product with given.
    """
    product = lfs_get_object_or_404(Product, pk=product_id)
    products = _get_filtered_products_for_product_view(request)
    paginator = Paginator(products, 25)
    page = paginator.page(request.REQUEST.get("page", 1))

    # Transform empty field / "on" from checkbox to integer
    data = dict(request.POST.items())
    if not product.is_variant():
        if data.get("active_base_price"):
            data["active_base_price"] = 1
        else:
            data["active_base_price"] = 0

    if product.sub_type == VARIANT:
        form = VariantDataForm(instance=product, data=data)
    else:
        form = ProductDataFormPatch(instance=product, data=data)

    if form.is_valid():
        form.save()
        if product.sub_type == VARIANT:
            form = VariantDataForm(instance=product)
        else:
            form = ProductDataFormPatch(instance=product)

        message = _(u"Product data has been saved.")
    else:
        message = _(u"Please correct the indicated errors.")

    form_html = render_to_string(template_name, RequestContext(request, {
        "product": product,
        "form": form,
        "redirect_to": lfs.core.utils.get_redirect_for(product.get_absolute_url()),
    }))

    html = [
        ["#selectable-products-inline", selectable_products_inline(request, page, paginator, product_id)],
        ["#data", form_html],
    ]

    result = simplejson.dumps({
        "html": html,
        "message": message,
    }, cls=LazyEncoder)

    return HttpResponse(result)


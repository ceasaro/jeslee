import lfs.core.widgets.image as lfs_image
import lfs.core.widgets.file as lfs_file
import lfs.manage.product.product as product
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from jeslee_web.lfs_patch.forms import CheckboxIntegerInput


def render_image_input(self, name, value, attrs=None):

        output = super(lfs_image.LFSImageInput, self).render(name, None, attrs=attrs)

        if value and hasattr(value, "url_60x60"):
            output += u"""<div><img src="%s" /></div>""" % value.url_60x60
        elif value and hasattr(value, "url"):
            output += u"""<div><img src="%s" /></div>""" % value.url

        if value:
            trans = _(u"Delete image")
            output += """<div><input type="checkbox" name="delete_image" id="id_delete_image" /> <label for="delete_image">%s</label></div>""" % trans._proxy____text_cast()

        return mark_safe(output)

# Monkey patch the LFSImageInput render method, cause it uses a non declared ugettext method '_proxy____unicode_cast'
# and we replace it with the '_proxy____text_cast' method
lfs_image.LFSImageInput.render = render_image_input


def render_file_input(self, name, value, attrs=None):
    output = super(lfs_file.LFSFileInput, self).render(name, None, attrs=attrs)
    if value:
        if hasattr(value, "url"):
            output = (u"""<div><a href="%s" />%s</a></div>""" % (value.url, value.name)) + output
        elif hasattr(value, "name"):
            output = (u"""<div>%s</div>""" % value.name) + output

    if value:
        trans = _(u"Delete file")
        output += """<div><input type="checkbox" name="delete_file" id="id_delete_file" /> <label for="delete_file">%s</label></div>""" % trans._proxy____unicode_cast()

    return mark_safe(output)

# Monkey patch the LFSFileInput render method, cause it uses a non declared ugettext method '_proxy____unicode_cast'
# and we replace it with the '_proxy____text_cast' method
lfs_file.LFSFileInput.render = render_image_input


old_init = product.ProductDataForm.__init__
def new_product_data_form_init(self, *args, **kwargs):
    old_init(self, args, kwargs)
    print "setting CheckboxIntegerInput widget"
    self.fields["active_base_price"].widget = CheckboxIntegerInput()

product.ProductDataForm
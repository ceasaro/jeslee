from django.forms import Select
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from jeslee_web.fashion_show.models import FashionShow

__author__ = 'ceasaro'


class SelectFashionShow(Select):

    def render_option(self, selected_choices, option_value, option_label):
        option_value = force_text(option_value)
        selected_html = ''
        if option_value in selected_choices:
            selected_html = mark_safe(' selected="selected"')
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        if option_value:
            fashion_show = FashionShow.objects.get(id=option_value)
            if not fashion_show.participate:
                selected_html += ' disabled="disabled"'

        return format_html('<option value="{0}"{1}>{2}</option>',
                           option_value,
                           selected_html,
                           force_text(option_label))


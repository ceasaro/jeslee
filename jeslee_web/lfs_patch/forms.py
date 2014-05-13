from django.forms.util import flatatt
from django.utils.encoding import force_text
from django.utils.html import format_html
from floppyforms.widgets import Widget

# Defined at module level so that CheckboxInput is picklable (#17976)
def boolean_check(v):
    return not (v is False or v is None or v == '')


class CheckboxIntegerInput(Widget):
    def __init__(self, attrs=None, check_test=None):
        super(CheckboxIntegerInput, self).__init__(attrs)
        # check_test is a callable that takes a value and returns True
        # if the checkbox should be checked for that value.
        self.check_test = boolean_check if check_test is None else check_test

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, type='checkbox', name=name)
        if self.check_test(value):
            final_attrs['checked'] = 'checked'
        if not (value is True or value is False or value is None or value == ''):
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(value)
        return format_html('<input{0} />', flatatt(final_attrs))

    def value_from_datadict(self, data, files, name):
        if name not in data:
            # A missing value means False because HTML form submission does not
            # send results for unselected checkboxes.
            return 0
        value = data.get(name)
        return 1 if value == 1 else 0

    # def _has_changed(self, initial, data):
    #     # Sometimes data or initial could be None or '' which should be the
    #     # same thing as False.
    #     if initial == 'False':
    #         # show_hidden_initial may have transformed False to 'False'
    #         initial = False
    #     return bool(initial) != bool(data)


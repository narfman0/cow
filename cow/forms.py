from django import forms

from .models import AddressPlugin, ImagePlugin, TextPlugin
from . import plugin_type_choices


class PluginCreateForm(forms.Form):
    plugin_type = forms.ChoiceField(choices=plugin_type_choices)

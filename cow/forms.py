from django import forms

from . import plugin_type_choices


class PluginCreateForm(forms.Form):
    plugin_type = forms.ChoiceField(choices=plugin_type_choices)

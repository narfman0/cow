from django import forms
from tinymce.widgets import TinyMCE

from .models import TextPlugin
from . import plugin_type_choices


class PluginCreateForm(forms.Form):
    plugin_type = forms.ChoiceField(choices=plugin_type_choices)


class TextPluginForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={
        'cols': 80,
        'rows': 30,
    }))

    class Meta:
        model = TextPlugin
        fields = ('content',)

from django import forms
from pastebin.models import Paste

class PasteForm(forms.ModelForm):
    class Meta:
        model = Paste
        fields = [
            'title',
            'language',
            'code_body',
        ]

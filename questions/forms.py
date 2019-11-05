from django import forms

from .models import Selected


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Selected
        fields = [
            'user',
            'question',
            'answer',
        ]


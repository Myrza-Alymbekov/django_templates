from django import forms

from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name.startswith('t'):
            raise forms.ValidationError("Names shold not start with 't'")
        return name

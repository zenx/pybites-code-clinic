from django import forms
from stats.models import Developer


class DeveloperCreateForm(forms.ModelForm):

    def clean_username(self):
        return self.cleaned_data['username'].lower()

    class Meta:
        model = Developer
        fields = ['username']

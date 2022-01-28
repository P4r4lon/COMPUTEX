from django import forms
from .models import Application, Supplier, Media

class applicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["stand", "name", "phone", "media"]


class supplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["name", "email"]


class mediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ["name"]

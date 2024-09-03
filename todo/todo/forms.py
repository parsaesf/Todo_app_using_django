from .models import TODOO
from django import forms


class TodoForm(forms.ModelForm):
    class Meta:
        model = TODOO
        fields = ["title", "status"]

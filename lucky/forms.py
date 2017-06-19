from lucky.models import Names
from django.forms import ModelForm


class NamesForm(ModelForm):
    class Meta:
        model = Names
        fields = ('name',)
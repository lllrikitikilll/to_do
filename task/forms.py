from django.forms import ModelForm
from .models import Ts

class TsForm(ModelForm):
    class Meta:
        model = Ts
        fields = ['title', 'description', 'date', 'done']
from django.forms import ModelForm, widgets
from .models import Ts
from django.forms.widgets import SelectDateWidget, TextInput
class TsForm(ModelForm):
    class Meta:
        model = Ts
        fields = ['title', 'description',"date", 'done']
    
        #widgets = {
         #       'date': SelectDateWidget(empty_label=('Выберите год', "Выберите месяц", "Выберите день"))}

from .models import Travel
from django.forms import ModelForm, TextInput

class TravelForm(ModelForm):
    class Meta:
        model = Travel
        fields = ["name", "mail", "phone_number", "place_of_chill"]
        widgets = {
            "name": TextInput(attrs={"type": "name", "placeholder": "Имя", "name": "name", "class": "input"}),
            "mail": TextInput(attrs={"type": "email", "placeholder": "E-Mail", "name": "email", "class": "input"}),
            "phone_number": TextInput(attrs={"type": "phone", "placeholder": "Телефон", "name": "number", "class": "input"}),
            "place_of_chill": TextInput(attrs={"type": "place", "placeholder": "Куда я хочу полететь?", "name": "place", "class": "input"}),
        }

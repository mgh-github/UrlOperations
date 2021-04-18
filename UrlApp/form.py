from django.forms import ModelForm
from .models import UrlForm, Search


class UserForm(ModelForm):
    class Meta:
        model = UrlForm
        fields = '__all__'

class SearchName(ModelForm):
    class Meta:
        model = Search
        fields = '__all__'


from django.forms import ModelForm
from .models import UrlForm, Search, Image


class UserForm(ModelForm):
    class Meta:
        model = UrlForm
        fields = '__all__'

class SearchName(ModelForm):
    class Meta:
        model = Search
        fields = '__all__'

class imgdown(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'


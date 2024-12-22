from django.forms import ModelForm
from viewer.models import Movie


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'  # Kasutab kõiki Movie välja andmeid.
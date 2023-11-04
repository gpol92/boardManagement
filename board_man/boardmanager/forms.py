from django.forms import ModelForm
from .models import Board

class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ('macAddress', 'status', 'where', 'defects', 'actions')
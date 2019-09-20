from django import forms
from .models import *

class NoticeForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'text',) 
        model = NoticeBoard
        
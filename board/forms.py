from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
        

class NoticeForm(forms.ModelForm):
    
        
    
    class Meta:
        # text = 

        fields = ['title','text']
 
        model = NoticeBoard

        widgets = {
                'title': forms.TextInput(
                    attrs={'class': 'form-control', 'style': 'width: 70%', 'placeholder': '제목을 입력하세요.'}
                ),
                # 'author': forms.Select(
                #     attrs={'class': 'custom-select'},
                # ),
                'text': forms.CharField(widget=CKEditorUploadingWidget()),
            }
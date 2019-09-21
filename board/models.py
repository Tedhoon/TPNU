from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField


class NoticeBoard(models.Model):
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    text = RichTextUploadingField()
    created_date = models.DateTimeField(auto_now_add=True)
    hits =  models.IntegerField(null=True, blank=True) #조회수

    def __str__(self):
        return self.title



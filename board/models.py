from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField

from django.contrib.auth.models import User


class NoticeBoard(models.Model):
    
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.CASCADE) # 유저 지워지면 다 지워지게
    text = RichTextUploadingField()
    created_date = models.DateTimeField(auto_now_add=True)
    hits =  models.PositiveIntegerField(default = 0) #조회수

    def __str__(self):
        return self.title
    
    @property
    def update_counter(self):
        self.hits += 1
        self.save()
    

    # class Meta:
    #     author_name =     


# from django.contrib.auth.models import User

# author = models.ForienKey(User, ondelete =True , null= True , default=1)
# class Comment(models.Model):
 
#     notice = models.ForeignKey(NoticeBoard, on_delete=True, null=True)
#     comment_date = models.DateTimeField(auto_now_add=True)
#     comment_user = models.TextField(max_length=20)
#     comment_thumbnail_url = models.TextField(max_length=300)
#     comment_textfield = models.TextField()

class FreeBoard(models.Model):
    
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.CASCADE) # 유저 지워지면 다 지워지게
    text = RichTextUploadingField()
    created_date = models.DateTimeField(auto_now_add=True)
    hits =  models.PositiveIntegerField(default = 0) #조회수

    def __str__(self):
        return self.title
    
    @property
    def update_counter(self):
        self.hits += 1
        self.save()
    
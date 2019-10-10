from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from hitcount.models import HitCountMixin ,HitCount
from django.contrib.contenttypes.fields import GenericRelation



class NoticeBoard(models.Model, HitCountMixin):
    
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.CASCADE) # 유저 지워지면 다 지워지게
    text = RichTextUploadingField()
    created_date = models.DateField(auto_now_add=True)
    hits =  models.PositiveIntegerField(default = 0) #사용자 계산용(실제 렌더링 수)
    hitcount = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation') # 실제 조회수

    def __str__(self):
        return self.title
    
    @property
    def update_counter(self):
        self.hits += 1
        self.save()
    

class FreeBoard(models.Model, HitCountMixin):
    
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.CASCADE) # 유저 지워지면 다 지워지게
    text = RichTextUploadingField()
    created_date = models.DateField(auto_now_add=True)
    hits =  models.PositiveIntegerField(default = 0) #조회수
    hitcount = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation')


    def __str__(self):
        return self.title
    
    @property
    def update_counter(self):
        self.hits += 1
        self.save()
    
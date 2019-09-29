from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User



class ImageBoard(models.Model):

    title = models.CharField(max_length = 50)
    author = models.ForeignKey(settings.AUTH_USER_MODEL , default=1, on_delete = models.CASCADE)
    # slug = models.SlugField(unique=True , blank =True)
    image = models.ImageField(upload_to='imageboard/')
    desc = models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True)
    hits =  models.PositiveIntegerField(default = 0) #조회수
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True ,related_name='post_likes')
    
    def __str__(self):
        return self.title
    
    @property
    def update_counter(self):
        self.hits += 1
        self.save()

    # @property
    # def total_likes(self):
    #     return self.likes.count() 


# class User(models.Model):

#     user = models.ForeignKey(User , on_delete = models.CASCADE)
#     like_posts = models.ManyToManyField('ImageBoard', blank=True, related_name='like_users')



        
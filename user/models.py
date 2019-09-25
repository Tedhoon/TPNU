from django.db import models
from django.contrib.auth.models import User
# from imageboard.models import *


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)



# class Like(models.Model):
#     # Blog의 through_fileds와 순서가 같아야 한다.
#     imagelike = models.ForeignKey(ImageBoard, on_delete = models.CASCADE, null = True)
#     user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)


# class User(models.Model):
	
#     likes = models.ManyToManyField(
#         User, # User 모델과 Blog 모델을 M:N 관계로 두겠다.
#         through = 'Like', # Like라는 중개 모델을 통해 M:N 관계를 맺는다.
#         through_fields = ('imagelike', 'user'), # Like에 blog 속성, user 속성을 추가하겠다.
#         related_name = 'likes' # 1:N 관계에서 blog와 연결된 comment를 가져올 때 comment_set으로 가져왔는데
#                                 # related_name을 설정하면 blog.like_set이 아니라 blog.likes로 like를 가져올 수 있다.
#     )

#     def like_count(self):
#         return self.likes.count() # 몇 개의 Likes와 연결되어 있는가를 보여주기 위한 메소드



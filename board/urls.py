from django.urls import path
from .views import *
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('notice/', notice , name='notice'),
    path('notice/detail/<int:notice_id>/', notice_detail, name = 'notice_detail'),
    path('notice/post/', notice_post , name = 'notice_post'),
]
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


from django.urls import path , include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('notice/', notice , name='notice'),
    path('notice/detail/<int:notice_id>/', notice_detail, name = 'notice_detail'),
    path('notice/post/', notice_post , name = 'notice_post'),
    path('notice/edit/<int:notice_detail_id>/' , notice_edit , name = 'notice_edit'),
    # path('notice/delete/<int:notice_detail.id>/' , notice_delete , name = 'notice_delete'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

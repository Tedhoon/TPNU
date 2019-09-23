from django.urls import path , include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
# from ckeditor_uploader import urls
from django.contrib.auth.decorators import login_required
from ckeditor_uploader import views as views_ckeditor
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('notice/', notice , name='notice'),
    path('notice/detail/<int:notice_id>/', notice_detail, name = 'notice_detail'),
    # path('notice/post/', notice_post , name = 'notice_post'),
    path('notice/post/', NoticePost.as_view() , name = 'notice_post'),
    path('notice/edit/<int:notice_detail_id>/' , notice_edit , name = 'notice_edit'),
    # path('notice/delete/<int:notice_detail_id>/' , notice_delete , name = 'notice_delete'),
    path('notice/delete/<slug:pk>/', NoticeDelete.as_view() , name = 'notice_delete'),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
   
    path('upload/', login_required(views_ckeditor.upload), name='ckeditor_upload'),
    path('browse/', never_cache(login_required(views_ckeditor.browse)), name='ckeditor_browse'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

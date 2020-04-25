from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ad/', admin.site.urls),
    path('', include('blog.urls')),
    #path('ckeditor/', include('ckeditor_uploader.urls'))
    path('tinymce/', include('tinymce.urls')),
]



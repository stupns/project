
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static # относится к ckeditor
from django.conf import settings # относится к ckeditor


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/',include('ckeditor.urls')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import re_path as url
from crudOps import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    url(r'^users$',views.UsersApi),
    url(r'^users/([0-9]+)$',views.FilesApi),

    url(r'^users/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
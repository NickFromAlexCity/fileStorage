from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('', views.FileListView.as_view(), name='list'),
    path('file/<int:pk>/', views.delete, name='delete'),
    path('upload/', views.FileUploadView.as_view(), name='upload'),

    path('admin/', admin.site.urls),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

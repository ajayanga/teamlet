from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs', views.blogs, name='blogs'),
    path('blogs/<int:pk>', views.blog, name='blog_detail'),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
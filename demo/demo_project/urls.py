from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from demo_project.demo_project.demo_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('demoapp.urls')),
    path('credentials/',include('credentialsapp.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
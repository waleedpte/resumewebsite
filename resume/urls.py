from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('resumesite.urls')),
    path('',include('cv.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

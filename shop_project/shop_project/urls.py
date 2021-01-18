from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop_app.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    # path('ckeditor', include('ckeditor_uploader.urls')),
]
#  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

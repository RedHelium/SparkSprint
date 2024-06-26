from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('apps.common.urls')),
    path("", include('apps.tasks.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, settings.STATIC_ROOT)

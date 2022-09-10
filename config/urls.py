from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView

# API URLS
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    # API base url
    path("api/", include("config.api_router")),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
]

if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from decentwork.apps.home.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    path('common/', include('decentwork.apps.common.urls')),
    path('cities/', include('decentwork.apps.common.urls')),
    path('professions/', include('decentwork.apps.common.urls')),
    path('', home),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Debug Toolbar.
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]

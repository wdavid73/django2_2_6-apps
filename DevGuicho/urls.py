from django.conf import settings
from django.conf.urls import url
from django.urls import path, include
from django.views.static import serve

urlpatterns = [
    path('', include('confma.urls', namespace="confma")),
    path('api/', include('confma_api.urls', namespace="confma_api")),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

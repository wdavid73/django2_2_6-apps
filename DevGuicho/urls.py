from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    path('', include('confma.urls_app', namespace="confma")),
    path('accounts/', include('django.contrib.auth.urls')),
]

# urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()
#
# if settings.DEBUG is False and settings.SANDBOX is True:
#     urlpatterns += patterns('',
#         url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
#             {'document_root': settings.STATIC_ROOT}),
#         url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#             {'document_root': settings.MEDIA_ROOT}),
#     )
#
# urlpatterns += patterns(
#     '',
#     url(r'^', include('cms.urls')),
# )


# if settings.DEBUG is True:
#     urlpatterns += staticfiles_urlpatterns()
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#
# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns = [
#     path('', views.index, name="index"),
#     path('confma/', include('confma.urls', namespace="confma")),
#     path('accounts/', include('django.contrib.auth.urls')),
# ]

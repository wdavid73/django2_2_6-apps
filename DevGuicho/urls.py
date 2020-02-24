from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

# urlpatterns = [
#     path('', views.index, name="index"),
#     path('confma/', include('confma.urls', namespace="confma")),
#     path('accounts/', include('django.contrib.auth.urls')),
# ]
urlpatterns = [
    # path('', views.index, name="index"),
    path('', include('confma.urls', namespace="confma")),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

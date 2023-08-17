from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('MyPetstagramProject.common.urls')),
    path('accounts/', include('MyPetstagramProject.accounts.urls')),
    path('pets/', include('MyPetstagramProject.pets.urls')),
    path('photos/', include('MyPetstagramProject.photos.urls')),
]

# това го правим като сетваме mediafiles - това реално ни дава достъп до mediafiles.
# Ако сме в DEBUG режим, тогава искам urlpatterns да ги увеличим
# На settings.MEDIA_URL искам да ми сложиш document_root=settings.MEDIA_ROOT
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

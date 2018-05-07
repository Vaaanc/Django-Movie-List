from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movie/', include('movie.urls', namespace='movie', app_name='movie'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

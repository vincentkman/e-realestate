from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import listings.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listings.views.home, name='home'), 
    path('about/', include('agent.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

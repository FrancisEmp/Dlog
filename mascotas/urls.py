from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/mascotasblog/', permanent=True)),
    path('mascotasblog/', include('mascotasblog.urls')),
]

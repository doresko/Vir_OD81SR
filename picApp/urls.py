from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

urlpatterns = [
    path('', include('pictures.urls')),
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', login_required(TemplateView.as_view(template_name="home.html"))),
]
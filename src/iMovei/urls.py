"""iMovei URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from iMovei.core import views
from iMovei.imoveis import urls as imoveis_urls
from iMovei.clientes import urls as clientes_urls
from iMovei.agenda import urls as agenda_urls


urlpatterns = [
    path('', views.home, name='home'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),

    path('clientes/', include(clientes_urls, namespace='clientes')),
    path('imoveis/', include(imoveis_urls, namespace='imoveis')),
    path('agenda/', include(agenda_urls, namespace='agenda'))
]

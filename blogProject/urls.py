"""blogProject URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ckeditor_uploader import views as views_ckeditor
from django.views.decorators.cache import never_cache
import blog.views
import disposal.views
import account.views
import board.views
import market.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.main, name='main'),
    path('be_geppetto/', include('blog.urls')),
    path('disposal/', include('disposal.urls')),
    path('account/', include('account.urls')),
    path('board/', include('board.urls')),
    path('market/', market.views.market, name="market"),
    path('market/<int:market_id>', market.views.detail4, name="detail4"),
    path('market/delete/<int:market_id>', market.views.delete4, name="delete4"), 
    path('market/new', market.views.marketpost, name="newblog"),
    path(r'^upload/', views_ckeditor.upload, name="ckeditor_upload"),
    path(r'^browse/', never_cache(views_ckeditor.browse),name='ckeditor_browse'),
]+static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )

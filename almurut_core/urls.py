"""
URL configuration for almurut_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path

from market.views import (HomeView, PublicationListView,
                          PublicationDetailView, FaqView,
                          ShoppingView, RegisterView,
                          LoginView, FavoritesView,
                          ErrorView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('publication-detail/', PublicationDetailView.as_view(), name='publication-detail-url'),
    path('home/', HomeView.as_view(), name='home-url'),
    path('publication-list/', PublicationListView.as_view(), name='publication-list-url'),
    path('shopping/', ShoppingView.as_view(), name='shopping-url'),
    path('register/', RegisterView.as_view(), name='register-url'),
    path('login/', LoginView.as_view(), name='login-url'),
    path('favorites/', FavoritesView.as_view(), name='favorites-url'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""prepare_be URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import os

from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.urls import path, include, re_path
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from django.template import loader


class ReactAppView(View):

    def get(self, request):
        try:
            with open(os.path.join(settings.BASE_DIR, 'build', 'index.html')) as file:
                return HttpResponse(file.read())
        except :
            return HttpResponse(
                """
                index.html not found ! build your React app !!
                """,
                status=501,
            )


urlpatterns = [
    re_path('^$', ReactAppView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('prepare_be.urls_api_v1'))
]

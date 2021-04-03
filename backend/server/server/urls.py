"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from apps.endpoints.views import decode, encode, homePage, hide,retrieve, statusMeter, statusId
from apps.steganography.test import myView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('test/', myView, name="test" ),
    path("decode/<int:id>", decode, name="decode"),
    path("encode/<int:id>", encode, name="encode"),
    path("status/", statusId, name="statusId"),
    path("status/<int:id>", statusMeter, name="statusMeter"),
    path("", homePage, name="homePage"),
    path("hide", hide, name="hide"),
    path("retrieve", retrieve, name="retrieve")
]

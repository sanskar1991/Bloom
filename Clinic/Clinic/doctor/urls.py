from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register('network', views.NetworkViewsets)
router.register('addsub', views.AddSubViewsets)
router.register('newexpo', views.NewExpoViewsets)

urlpatterns = [
    path('', include(router.urls)),
]

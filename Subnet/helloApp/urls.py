from django.urls import path

from . import views
# index, network_list, add_sub_list


urlpatterns = [
    path('', views.index, name="index"),
    path('network/', views.network_list, name="network_list"),
    path('addsub/', views.add_sub_list, name="add_sub_list"),
    path('newexpo/', views.new_exposure, name="new_exposure"),
]

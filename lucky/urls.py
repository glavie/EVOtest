from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^add_name/$', views.add_name, name='add_name'),
    url(r'^names_list/', views.names_list, name='names_list'),
    url(r'^del_name/', views.del_name, name='del_name'),
    url(r'^pick_luckers', views.rand_names, name='rand_names'),
]
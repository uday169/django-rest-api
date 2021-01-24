from django.conf.urls import url
from customers import views

urlpatterns = [
    url(r'^customers/$', views.customer_list),
    url(r'^customers/(?P<pk>[0-9]+)$', views.customer_detail),
]
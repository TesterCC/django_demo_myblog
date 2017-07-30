# from django.conf.urls import url, include
#
#
# urlpatterns = [
#     url(r'^index/', include('blog.urls')),
# ]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index),
]

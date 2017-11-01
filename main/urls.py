__author__ = 'mrs Ojoodide'
from django.conf.urls import url
from . import views
urlpatterns = [
     url(r'', views.index, name='index'),
    # url(r'^profile', views.Home.as_view())
      # URL for the index page in which you sign-in

    # URL for logging the user in
    url(r'^profile', views.sign_in, name='sign_in'),
]

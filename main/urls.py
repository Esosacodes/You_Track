__author__ = 'mrs Ojoodide'
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^profile', views.sign_in, name='signin'),
    url(r'^map', views.show_location_on_map, name='location'),
    
     url(r'', views.index, name='index'),
    # url(r'^profile', views.Home.as_view())
      # URL for the index page in which you sign-in

    # URL for logging the user in
]

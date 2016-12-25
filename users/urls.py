from django.conf.urls import patterns, url
from .views import complete_registration


urlpatterns = patterns('',
    url(r'^complete_registration/$', complete_registration, name='users_complete_registration'),
    url(r'^login$', 'users.views.login', name='login'),
    url(r'^logout/$', 'users.views.logout', name='users_logout'),
)
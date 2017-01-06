from django.views.generic import TemplateView
from django.conf.urls import patterns, url, include
from django.contrib.auth import urls as django_auth_urls

from users import views as users_views


urlpatterns = [
    url(r'^login/$', users_views.login, name='login'),
    url(r'^logout/$', users_views.logout, name='logout'),
    url(r'^register/$', users_views.register, name='register'),
    url(r'^profile/$', TemplateView.as_view(template_name='profile.html'), name='profile'),
    url('^', include(django_auth_urls)),
]
from django.views.generic import TemplateView
from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
    url(r'^login/$', 'users.views.login', name='login'),
    url(r'^logout/$', 'users.views.logout', name='logout'),
    url(r'^register/$', 'users.views.register', name='register'),
    url(r'^register/complete/$', 'users.views.complete_registration', name='complete_reg'),
    url(r'^profile/$', TemplateView.as_view(template_name='profile.html'), name='profile'),
    url('^', include('django.contrib.auth.urls')),
)
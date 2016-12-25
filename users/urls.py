from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^register/$', 'users.views.register', name='register'),
    url(r'^register/complete/$', 'users.views.registration_complete', name='registration_complete'),
    url('^', include('django.contrib.auth.urls')),
)
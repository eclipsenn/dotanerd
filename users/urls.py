from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.contrib.auth import views as django_auth_views
from users import views as users_views

from registration.backends.hmac import views as hmac_views

two_phase_urlpatterns = [
    # This one should be defined before the DotanerdActivationView url cause it's the same regex
    url(r'^activate/complete/$',
        TemplateView.as_view(
            template_name='registration/activation_complete.html'
        ),
        name='registration_activation_complete'),
    # url for overrided DotanerdActivationView
    url(r'^activate/(?P<activation_key>[-:\w]+)/$',
        users_views.DotanerdActivationView.as_view(),
        name='registration_activate'),
    url(r'^register/$',
        hmac_views.RegistrationView.as_view(),
        name='registration_register'),
    url(r'^register/complete/$',
        TemplateView.as_view(
            template_name='registration/registration_complete.html'
        ),
        name='registration_complete'),
]

urlpatterns = [
    url(r'^login/$', django_auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', django_auth_views.logout,{'template_name': 'home.html'}, name='logout'),

    # currently unused as two-phase registration is implemented. Can be activated if needed.
    url(r'^register/$', users_views.register, name='register'),

    url(r'^profile/$', users_views.profile, name='profile'),
    url(r'^cropping/$', TemplateView.as_view(template_name='cropping.html'), name='cropping'),

    url(
        r'^password_change/$',
        django_auth_views.password_change,
        {
            'template_name': 'change_password.html',
            'post_change_redirect': 'pass_change_done',
        },
        name='pass_change'
    ),
    url(
        r'^update_profile/$', users_views.update_profile,
        {'template_name': 'update_profile.html'},
        name='update_profile'
    ),
    url(
        r'^password_change_done/$',
        django_auth_views.password_change_done,
        {'template_name': 'change_password_done.html'},
        name='pass_change_done'
    ),
    url(r'^2phase/', include(two_phase_urlpatterns)),
]

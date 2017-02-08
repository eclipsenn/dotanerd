from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


import questions.views
admin.autodiscover()

urlpatterns = [
    url(r'^$', questions.views.index, name='index'),
    url(r'^questions/$', questions.views.ListQuestionView.as_view(), name='questions-list',),
    url(r'^questions/(?P<pk>\d+)$', questions.views.QuestionDetails.as_view(), name='question-details',),
    url(r'^questions/(?P<pk>\d+)/answer/$', questions.views.ask_question_view, name='questions-ask'),
    url(r'^dotanerd/$', questions.views.ask_question_view, name='questions-ask'),
    url(r'^users/', include('users.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR)
urlpatterns += staticfiles_urlpatterns()

from django.conf.urls import patterns, url

from chess.apps.etudes.views import EtudesListView, EtudesByAuthor


urlpatterns = patterns('chess.apps.etudes.views',
    url(r'^$', EtudesListView.as_view(), name='etudes_list'),
    url(r'^(?P<author_slug>\w*)/$', EtudesByAuthor.as_view(),
        name='author_etudes'),
)
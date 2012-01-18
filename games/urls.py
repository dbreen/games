from django.conf import settings
from django.conf.urls.defaults import *


urlpatterns = patterns('games.core.views',
    url('^$', 'home', name='home'),
    url('^game/(?P<game_id>\d+)/details/$', 'game_details', name='game_details'),
)

from django.contrib import admin
admin.autodiscover()

urlpatterns += patterns('',
    (r'^djadmin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )

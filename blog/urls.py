from django.conf.urls import url,patterns,include


from . import views
from django.conf import settings

'''
if settings.DEBUG == True:
   urlpatterns += patterns(
       '',
       url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
       url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
   )

'''

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^blog/page-(?P<page_id>[0-9]+)$',views.homepaginator,name='homepaginator'),
    url(r'^blog/(?P<nav_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^blog/(?P<nav_id>[0-9]+)/page-(?P<page_id>[0-9]+)$',views.detailpaginator,name='detailpaginator'),
    url(r'^blog/(?P<nav_id>[0-9]+)/(?P<context_id>[0-9]+)/$',views.contextDetail,name='contextDetail'),
    url(r'^blog/aboutme/$',views.aboutme,name='aboutme'),
    url(r'^blog/hitcount/',include('hitcount.urls',namespace='hitcount')),
]
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}))
#url(r'^media/(?P<media_id>)',views.media,name='media'),
#url(r'^(?P<nav_id>[0-9]+)/$',views.detail,name='detail'),
#url(r'^(?P<nav_id>[0-9]+)/(?P<context_id>[0-9]+)/$',views.contextDetail,name='contextDetail'),
#url(r'^(?P<nav_id>[0-9]+)-(?P<page_id>[0-9]+)/$',views.paginator,name='paginator'),
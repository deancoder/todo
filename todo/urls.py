from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
      url(r'^$', 'dailytask.views.index', name='index'),
      url(r'^home', 'dailytask.views.home', name='home'),
      url(r'^dairy$', 'dailytask.views.dairy', name='dairy'),
      url(r'^profile$', 'dailytask.views.profile', name='profile'),
      #url(r'^blog/', include('dailytask.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

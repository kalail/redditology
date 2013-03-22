from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('scraper.views',
	url(r'^$', 'index'),
	)
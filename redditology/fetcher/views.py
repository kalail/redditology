from django.shortcuts import render_to_response
from django.template import RequestContext
# from scraper.models import Scrape
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse


# def index(request):
	# """Index Page

	# Scraper page showing statistics about scrapes.

	# """
	# Collect scrapes
	# scrapes = Scrape.objects.all().order_by('created_on')
	# first_scrape = scrapes[0]
	# return render_to_response('scraper/index.html', {'scrapes': scrapes, 'first_scrape': first_scrape}, context_instance=RequestContext(request))
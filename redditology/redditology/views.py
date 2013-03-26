from django.shortcuts import render_to_response
from django.template import RequestContext
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse


def index(request):
	"""Index Page

	Landing page for the website.

	"""
	# Collect data for index page
	return render_to_response('index.html', context_instance=RequestContext(request))
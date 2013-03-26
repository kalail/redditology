from fabric.api import *

# Import settings
env.hosts = [
	'96.126.122.107',
]


def full_clean():
	"""Clean the current local environment"""

	# Remove logs
	local('rm ../logs/master.log')
	local('rm ../logs/info.log')
	# Remove database
	local('rm redditology.db')
	# Delete celery files
	local('rm ../celerybeat-schedule')

def deploy():
	"""Fully deploy the app to heroku, running all the steps."""

	run('workon redditology')
	run('cdvirtualenv')
	with cd(redditology):
		run('git pull master')
		run('python redditology/manage.py syncdb')
		run('python redditology/manage.py migrate')
		run('python redditology/manage.py collectstatic')
		run('foreman start & disown')


def compile_coffee():
	"""Compile coffeescript files to javascript"""

	# Get files with .coffee extension
	files = local("find static/js -name *.coffee", capture=True).split("\n")
	for f in files:
		print('compiling %s...' % f)
		local('coffee -c %s' % f)

def watch_coffee():
	"""Watch and automatically compile coffeescript files to javascript""" 

	# Get files with .coffee extension
	coffee_folder = 'static/coffee'
	js_folder = 'static/js'
	print('watching %s for changes' % coffee_folder)
	local('coffee -o %s -wc %s' % (js_folder, coffee_folder))

def watch_less():
	"""Watch and automatically compile coffeescript files to javascript"""

	# Get files with .less extension
	less_folder = 'static/css'
	print('watching %s for changes' % less_folder)
	local('watch-less -d %s -e .css' % less_folder)
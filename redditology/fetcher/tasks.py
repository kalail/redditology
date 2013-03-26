import praw
import pytz
from celery.utils.log import get_task_logger
from django.core.cache import cache
from celery.task import task
from datetime import datetime
from posts.models import Post, PostSnapshot
from .models import Fetch


logger = get_task_logger(__name__)


@task
def fetch_posts():
	"""Fetch Posts

	Fetch the current top 100 posts on the reddit homepage using the PRAW package and then dispatch the tasks to save the posts.

	"""
	logger.info('Fetching front page posts')
	reddit = praw.Reddit(user_agent='Redditology - Front Page Posts Fetcher')
	# Fetch posts
	fetch = Fetch.objects.create()
	try:
		posts = reddit.get_front_page(limit=100)
	except Exception:
		logger.error('Error fetching posts!')
		fetch.successful = False
	else:
		logger.info('Done')
		fetch.successful = True
	finally:
			fetch.save()
	# Exit if failed
	if not fetch.successful:
		return
	# Send save post tasks
	logger.info('Dispatching save tasks')
	for idx, post in enumerate(posts):
		# Correct rank offset
		rank = idx + 1
		# Create parsed post
		post_cache_key = '%s - %s' % (post, post.id)
		cache.set(post_cache_key, post)
		save_fetched_post.delay(post_cache_key, rank,  fetch.id)
		logger.info('Sent rank %s post task' % rank)


@task
def save_fetched_post(post_cache_key, rank, fetch_id):
	"""Save Fetched Post

	Extracts fetched post from the cache to update the post properties and create snapshots of time varying post data in the database.

	"""
	# Get post from cache
	post = cache.get(post_cache_key, None)

	# Check for existence
	if not post:
		logger.error('Post not in cache')
		return

	# Consume post
	cache.delete(post_cache_key)

	# Get or create post model
	try:
		p = Post.objects.get(id=post.id)
	except Post.DoesNotExist:
		p = Post(id=post.id)
	# Update all fields
	p.title = post.title
	p.author = post.author
	p.url = post.url
	p.domain = post.domain
	p.over_18 = post.over_18
	p.subreddit = post.subreddit
	p.domain = post.domain
	p.created_on_reddit = datetime.utcfromtimestamp(p.created_on).replace(tzinfo=pytz.UTC)
	p.save()

	fetch = Fetch.objects.get(id=fetch_id)

	post_snapshot = PostSnapshot(
		# Relations
		post = p,
		fetch = fetch,
		# Time data
		up_votes = post.ups,
		down_votes = post.downs,
		rank = rank,
		num_comments = post.num_comments
	)
	post_snapshot.save()

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'redditology.settings'

import pdb
import matplotlib.pyplot as plt
from redditology.models import Post, Snapshot, PostSnapshot
import pickle

if __name__ == '__main__':
	try:
		with open('data.pkl', 'rb') as f:
			data = pickle.load(f)
	except IOError:
		snapshots = Snapshot.objects.all().order_by('created_on')[0:400]
		posts = Post.objects.all()
		data = {}
		for p in posts:
			data[p.id] = []
		for snapshot in snapshots:
			for p in posts:
				try:
					ps = snapshot.postsnapshot_set.get(post=p.id)
					data[p.id].append(ps.rank)
				except PostSnapshot.DoesNotExist:
					data[p.id].append(113)
				except PostSnapshot.MultipleObjectsReturned:
					ps = snapshot.postsnapshot_set.filter(post=p.id)[0]
					data[p.id].append(ps)

		with open('data.pkl', 'wb') as f:
			pickle.dump(data, f)	

	for key in data:
		point = data[key]
		for idx, p in enumerate(point):
			if type(p) != int:
				point[idx] = point[idx-1]
		plt.plot(point)
	plt.ylabel('Rank')
	plt.xlabel('Time')
	plt.savefig('test_correct.png')

	# Dupicate post snapshots of post-12uwjh
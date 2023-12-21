from django.test import TestCase
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'inflearn.settings'
os. environ['DJANGO_ALLOW_ASYNC_UNSAGE'] = 'true'

import django
django.setup()

from instagram.models import Post,Comment
comment = Comment.objects.first()

print(comment)

post_get = Post.objects.get(pk=comment.post_id)
print(post_get)

post = Post.objects.first()
print(post)

post.comment_set.all()





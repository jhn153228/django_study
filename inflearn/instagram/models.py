from django.db import models
from django.conf import settings

class User(models.Model):
    pass

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True) # 필수 유무 = blank
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # java의 toString,
    def __str__(self):
        # return f"Custom Post object ({self.id})"
        return self.message

    class Meta:
        ordering = ['-id']

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = '메시지 글자수'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             limit_choices_to={'is_public': True})
    # post = models.ForeignKey('instagram.Post', on_delete=models.CASCADE)     // 다른 DB에 있는 Post를 외래키로 지정할 때 사용
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pass

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post)

    def __str__(self):
        return self.name

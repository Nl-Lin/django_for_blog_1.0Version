from django.db import models
from django.contrib.auth.models import User
from blog.models import Article
# Create your models here.


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', default='')  # 被评论的文章
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  # 评论者
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]


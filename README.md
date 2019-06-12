# django_for_blog_1.0Version


# 一级评论
```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', default='')  # 被评论的文章
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  # 评论者
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]
```
comment/models.py

# 分页
```python
  def Pagination(self, post_list, page):  # 分类器,分类函数
        paginator = Paginator(post_list, self.per_page)
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)
        return post_list
```    
blog/views.py

# markdown

```python
def MD():
    return markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        TocExtension(slugify=slugify),
    ])
``` 
blog/views.py

> 溜了~溜了~

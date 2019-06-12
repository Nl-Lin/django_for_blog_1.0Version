from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from mdeditor.fields import MDTextField
# Create your models here.


class Tag(models.Model):
    '''
    文章标签
    '''

    name = models.CharField(max_length=20, unique=True, verbose_name=u'标签')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name

class Article(models.Model):
    '''
    博客文章，属性段
    '''

    title_name = models.CharField(max_length=36, verbose_name=u'标题')
    body = MDTextField(verbose_name=u'正文')
    # 创建时间与修改时间
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间',)
    # 文章标签: 一篇文章可以拥有多个标签 ，即一对多关系
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')
    # 文章作者: 一篇文章只能对应一个作者，即一对一关系
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u'作者')
    # 文章访问量
    views = models.PositiveIntegerField(default=0, verbose_name=u'阅读数')
    # 文章是否指定，默认不置顶
    is_top = models.BooleanField(default=False, verbose_name=u'置顶')
    # 文章发布状态，默认创建成功不发布。
    is_show = models.BooleanField(default=False, verbose_name=u'发布状态')

    post_type = models.CharField(max_length=20, choices=(('post', u'博客文章'),
                                                        ('about', u'关于页面'),
                                                        ('project', u'我的项目')
                                                        ), default='post', verbose_name=u'类型')

    def __str__(self):
        return self.title_name

    def get_absolute_url(self):
        return reverse('blog_app:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        # 获取 Post 列表时，按照顶置、创建时间排序
        ordering = ['-is_top', '-created_time']
        verbose_name = u'文章'
        verbose_name_plural = u'文章'



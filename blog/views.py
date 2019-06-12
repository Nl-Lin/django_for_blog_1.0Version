from django.shortcuts import render, get_object_or_404, redirect
import markdown
from django.views.generic import ListView
from .forms import RegitserForm
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Article, Tag
from django.db.models.aggregates import Count
from comment.models import Comment
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
# Create your views here.


def page_not_found(request):
    return render(request, 'blog/404.html')


def MD():
    return markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        TocExtension(slugify=slugify),
    ])


class Index():  # 博客文章首页
    def __init__(self):
        self.per_page = 3   # 指定每个页面显示文章数量

    def index(self, request):  # 首页函数
        post_list = Article.objects.filter(is_show=True, post_type='post')  # 筛选指定类型
        page = request.GET.get('page')
        return self.get_data(post_list=post_list, page=page, request=request)

    def category(self, request, category):  # 分类函数
        post_list = Article.objects.filter(category=category, post_type='post')  # 筛选分类
        page = request.GET.get('page')
        return self.get_data(post_list=post_list, page=page, request=request)

    def tags(self, request, tag):  # 标签函数
        post_list = Article.objects.filter(tags__name=tag, is_show=True, post_type='post')  # 标签筛选
        page = request.GET.get('page')  # 获取当前页
        return self.get_data(post_list=post_list, page=page, request=request)

    def get_data(self, post_list, page, request):  # 数据整合函数
        post_list = self.Pagination(post_list=post_list, page=page)
        for i in range(len(post_list)):
            md = MD()
            post_list[i].body = md.convert(post_list[i].body)  # markdown 渲染
            post_list[i].toc = md.toc
        return render(request, 'blog/index.html', context={'post_list': post_list})

    def Pagination(self, post_list, page):  # 分类器,分类函数
        paginator = Paginator(post_list, self.per_page)
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)
        return post_list

    def Show_more_tags(self, request):
        tags = Tag.objects.all()
        return render(request, "blog/index.html", context={"all_tags": tags})

# 博客详情页


class Detail(View):

    def get(self, request, pk):
        post = get_object_or_404(Article, pk=pk)
        md = MD()
        post.body = md.convert(post.body)
        post.toc = md.toc
        post.increase_views()  # 统计访问量
        comments = Comment.objects.filter(article=pk)  # 取出评论的id
        return render(request, 'blog/detail.html', locals())


# 归档页面


def Arcives(request):
    years = Article.objects.filter(is_show=True, post_type='post').dates('created_time', 'year', order='DESC')
    post_list = Article.objects.filter(is_show=True, post_type='post').order_by('-created_time')
    return render(request, 'blog/archives.html', context={'years': years, 'post_list': post_list})

# 标签


def Tags(request):
    tags = Tag.objects.filter(article__is_show=True, article__post_type='post').annotate(num_posts=Count('post')).filter(num_posts_gt=0).order_by('-num_posts')
    return render(request, 'blog/tags.html', context={'tags': tags})

# 搜索请求


class Search(ListView):
    model = Article
    context_object_name = 'object_list'
    template_name = 'blog/search.html'

    def get_queryset(self):
        key = self.request.GET["key"]
        if key:
            return Article.objects.filter(Q(title_name__icontains=key) | Q(body__icontains=key), is_show=True,
                                          post_type="post")
        else:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["key"] = self.request.GET["key"]
        return context


# 注册用户
def register(request):
    if request.method == 'POST':
        form = RegitserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegitserForm
    return render(request, 'blog/register.html', locals())





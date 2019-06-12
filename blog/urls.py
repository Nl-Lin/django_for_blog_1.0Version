from django.urls import path
from blog import views
app_name = 'blog_app'

urlpatterns = [
    # 主页路由
    path('', views.Index().index, name='index'),
    path('tags/', views.Index().tags, name='Tags'),
    path('archives/', views.Arcives, name='Archives'),
    path('category/', views.Index().category, name='category'),
    path('tags/<tag>/', views.Index().tags, name='tags'),
    # 详情页路由
    path('detail/<int:pk>/', views.Detail.as_view(), name='detail'),  # reverse 指定 第一个参数 设置为 app_name:name
    # 文章搜索路由
    path('search/', views.Search.as_view(), name='search'),
    # 注册路由
    path('register/', views.register, name='register'),


]

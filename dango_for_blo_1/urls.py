"""dango_for_blo_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

app_name = 'user'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # 导入其它blog下的urls
    path('comment/', include('comment.urls')),
    path('mdeditor/', include('mdeditor.urls')),  # 富文本编辑器，记得在setting.py文件注册

    # 将 auth 应用中的urls 模块包含进来
    path('users/', include('django.contrib.auth.urls'))
#     包含这么多
# users/login/$ [name='login']
# ^users/logout/$ [name='logout']
# ^users/password_change/$ [name='password_change']
# ^users/password_change/done/$ [name='password_change_done']
# ^users/password_reset/$ [name='password_reset']
# ^users/password_reset/done/$ [name='password_reset_done']
# ^users/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
# ^users/reset/done/$ [name='password_reset_complete']
]


"""PyWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin,auth
from django.urls import path,include
from django.conf.urls import url
from bookstore import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name = 'index'),
    path('test/load/', views.check , name = 'check'),
    path('reloading/',views.reload,name='reload'),
    path('test/', views.test , name = 'test'),
    path('publish/', views.publish, name='publish'),
    path('publish/publishing', views.publishing, name='publishing'),
    path('publishdt/publishingdt', views.publishingdt, name='publishingdt'),
    path('archive/',views.archive,name='archive'),
    path('archive/note/<slug:article_id>' , views.get_detail_page),
    path('article-delete/<slug:article_id>/', views.article_delete, name='article_delete'),
    path('blog/' , include('bookstore.urls')),
    path('login/' , views.log , name = 'log'),
    path('logout/', views.logout , name = 'logout'),
    path('search/', views.search , name = 'search'),
    path('Register/', views.Register , name = 'Register'),
    url(r'^users/', include('django.contrib.auth.urls')),

]

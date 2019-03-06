#from django.conf.urls import url
from django.urls import path
from blog.views import *


app_name = 'blog'
urlpatterns = [
    # Example: /
    #url(r'^$', PostLV.as_view(), name='index'),
    path('', PostLV.as_view(), name='index'),

    # Example: /post/ (same as /)
    #url(r'^post/$', PostLV.as_view(), name='post_list'),
    path('post/', PostLV.as_view(), name='post_list'),

    # Example: /post/django-example/
    #url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),
    path('post/<slug>/', PostDV.as_view(), name='post_detail'),

    # Example: /archive/
    #url(r'^archive/$', PostAV.as_view(), name='post_archive'),
    path('archive/', PostAV.as_view(), name='post_archive'),

    # Example: /2012/
    #url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),
    path('<int:year>/', PostYAV.as_view(), name='post_year_archive'),

    # Example: /2012/nov/
    #url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),
    path('<int:year>/<str:month>/', PostMAV.as_view(), name='post_month_archive'),

    # Example: /2012/nov/10/
    #url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),
    path('<int:year>/<str:month>/<int:day>/', PostDAV.as_view(), name='post_day_archive'),

    # Example: /today/
    #url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),
    path('today/', PostTAV.as_view(), name='post_today_archive'),

    # Example: /tag/
    #url(r'^tag/$', TagTV.as_view(), name='tag_cloud'),
    path('tag/', TagTV.as_view(), name='tag_cloud'),

    # Example: /tag/tagname/
    #url(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),
    path('tag/<str:tag>/', PostTOL.as_view(), name='tagged_object_list'),

    # Example: /search/
    #url (r'^search/$', SearchFormView.as_view(), name='search'),
    path('search/', SearchFormView.as_view(), name='search'),

    # Example: /add/
    path('add/',
         PostCreateView.as_view(), name="add",
    ),

    # Example: /change/
    path('change/',
         PostChangeLV.as_view(), name="change",
    ),

    # Example: /99/update/
    path('<int:pk>/update/',
         PostUpdateView.as_view(), name="update",
    ),

    # Example: /99/delete/
    path('<int:pk>/delete/',
         PostDeleteView.as_view(), name="delete",
    ),
]
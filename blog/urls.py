from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', posts, name='posts_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<det_slug>/', post_detail, name='post_detail_url'),
    path('post/<det_slug>/update', PostUpdate.as_view(), name='post_update_url'),
    path('post/<det_slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<det_slug>/', tag_detail, name='tag_detail_url'),
    path('tag/<det_slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<det_slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
]

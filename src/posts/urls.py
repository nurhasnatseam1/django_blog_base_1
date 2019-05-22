from django.urls import path
from .views import (
    posts_home,
    posts_create,
    posts_delete,
    posts_update,
    posts_detail,

)

#app name
app_name='posts'

urlpatterns=[
    path('',posts_home,name='posts_home'),
    path('create/',posts_create,name='posts_create'),
    path('delete/<int:post_id>/',posts_delete,name='posts_delete'),
    path('update/<int:post_id>/',posts_update,name='posts_update'),
    path('detail/<int:post_id>/',posts_detail,name='posts_detail'),
]
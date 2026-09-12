from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('',views.index ,name='index'),
    path('posts/',views.post_list,name='post_list'),
    path('posts/<str:slug>/',views.post_detail,name='post_detail'),
    path('about-us/',views.about_us,name='about_us'),
    path('posts/<str:slug>/comment',views.post_comment,name='post_comment'),
    path('profile/',views.profile,name='profile'),
    path('profile/create_post',views.create_post,name='create_post'),
]

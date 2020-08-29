from django.urls import path

from . import views
 
 
urlpatterns =[
     
     path('', views.index, name='index'),
     path('blogs/', views.listBlog, name='blogs'),
     path('detail/<str:pk>', views.detailBlog, name='detail'),

     #CRUD
     path('create-post/', views.createPost, name='create'),
     path('update-post/<str:pk>', views.updatePost, name='update'),
     path('delete/<str:pk>', views.deletePost, name='delete')


 ]
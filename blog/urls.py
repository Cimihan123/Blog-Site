from django.urls import path

from . import views
 
app_name = 'blog' # good pattern to have a blog name.
 
urlpatterns =[
     
     path('', views.index, name='index'),
     path('blogs/', views.listBlog, name='blogs'),
     path('detail/<str:pk>', views.detailBlog, name='detail'),

     #CRUD
     path('create-post/', views.createPost, name='create'),
     path('update-post/<int:pk>', views.updatePost, name='update'),
     path('delete/<int:pk>', views.deletePost, name='delete')


 ]
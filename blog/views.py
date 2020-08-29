from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.contrib import messages
from .filters import *
from django.core.paginator import Paginator ,PageNotAnInteger,EmptyPage
# Create your views here.


def index(request):

    template_name = 'index.html'

 

    skill = Skill.objects.all()[:8]



    post = Post.objects.order_by('-date')[:3]

    contact = contactForm()
    if request.method == 'POST':
        contact = contactForm(request.POST)
        if contact.is_valid:
            contact.save()
            return redirect('index')
        else:
            messages.error(request, "Error")
     
    context = {
      
        'skills' : skill,
        'posts' : post,
        'contact' : contact,
       }

    return render(request,template_name,context)





def listBlog(request):

    template_name = 'blog.html'
    recent_posts = Post.objects.order_by('-date')[:5]

    post = Post.objects.all()
    f = PostFilter(request.GET,queryset=post)
    poste = f.qs
 

    paginator = Paginator(poste, 4) # Show 25 contacts per page.

    page = request.GET.get('page')
   
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
       page_obj = paginator.page(paginator.num_pages)
    
    
   

    context = {

        'posts' : page_obj,
        'recent_posts' : recent_posts,
        'filter' : f,
       
    }

    return render(request,template_name,context)



def detailBlog(request,pk):

    template_name = 'blog-detail.html'

    
    recent_posts = Post.objects.order_by('-date')[:5]
    post = Post.objects.get(pk=pk)
    comment = Comment.objects.filter(post=post)
    posts = Post.objects.all()
  



    comment_form = commentForm()
    if request.method == 'POST':
        comment_form = commentForm(request.POST)
        if comment_form.is_valid():
            comments = comment_form.save(commit=False)

            comments.post = post
            comments.save()
            return redirect('detail',pk=pk)

    context = {

        'posts' : post,
        'comment_form' : comment_form,
        'comments' : comment,
        'recent_posts' : recent_posts,
   
      
    }

    return render(request,template_name,context)



def createPost(request):


    template_name = 'update.html'

    
    Pform = postForm(request.POST,request.FILES)
    if request.method == 'POST':
        Pform = postForm(request.POST,request.FILES)
        if Pform.is_valid():
            Pform.save()
            return redirect('blogs')
    

    context = {

        'Pform' : Pform,
    }

    return render(request,template_name,context)




def updatePost(request,pk):


    template_name = 'update.html'

    post = Post.objects.get(pk=pk)
    Pform = postForm(instance=post)
    if request.method == 'POST':
        Pform = postForm(request.POST,request.FILES,instance=post)
        if Pform.is_valid():
            Pform.save()
            return redirect('blogs')


    context = {

        
        'Pform' : Pform,
    }

    return render(request,template_name,context)


def deletePost(request,pk):
    template_name = 'blog-detail.html'

    post = Post.objects.get(pk=pk)
    if post:
        post.delete()
        return redirect('blogs')

   

    return render(request,template_name)
    
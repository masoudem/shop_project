from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import *
from django.views.generic import TemplateView,ListView,DetailView
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from market_user.models import CustomUser
from django.contrib.auth.views import LogoutView
from django.template.defaultfilters import slugify, time
from django.db.models import Q
from django.contrib import messages
import time

class PostList(ListView):
    model = Post
    template_name = "post_list.html"
    
    def get_context_data(self, **kwargs):
        context_data = {}
        context_data = super().get_context_data(**kwargs)

        context_data['post'] = Post.objects.all()
        context_data['post_img'] = Post.objects.order_by('-post_date')[:4]
        
        return context_data

        
def post_detail(request, slug):
    post=Post.objects.get(slug=slug)

    form = CommentForm(None or request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        form = CommentForm()        
    return render(request, 'post_detail.html', {'post':post, 'form': form})
    
    
class CategoryList(ListView):
    model = Category
    template_name = "category_list.html"
    
    
def category_detail(request, id):
    category = Post.objects.filter(category__id = id).all()
    return render(request, 'category_detail.html', {'category':category})


class TagList(ListView):
    model = Tag
    template_name = "tag_list.html"
    
    
def tag_detail(request, id):
    tag = Post.objects.filter(tag__id = id).all()
    return render(request, 'tag_detail.html', {'tag':tag})


def mylogin(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = authenticate(request,username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                print(user)
                login(request,user)
                messages.success(request, 'وارد شدید!')
                return redirect(reverse('posts'))
            else :
                messages.success(request, 'your password is not correct!')
    return render(request,'forms/login.html',{'form':form})

def myRegister(request):
    form = UserFormModel(None or request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = CustomUser.objects.create_user(phone_number=form.cleaned_data['phone_number'],email=form.cleaned_data['email'],password=form.cleaned_data['password'])
            print('new user register is :',user)
            return redirect(reverse('login'))
    
    return render(request,'forms/register.html',{'form':form})


def update_post(request, slug):
    context ={}
    
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect(reverse('posts'))
    else:
        form = PostForm(instance=post)        
    context['form'] = form
    return render(request, 'forms/update_post.html', context)


def update_category(request, id):
    context ={}
    
    category = Category.objects.get(id=id)
    
    form = CategoryForm(None or request.POST, instance=category)
    
    if form.is_valid():
        form.save()
        return redirect(reverse('all_category'))
    context['form'] = form
    return render(request, 'forms/update_category.html', context)


def update_tag(request, id):
    context ={}
    
    tag = Tag.objects.get(id=id)
    
    form = TagForm(None or request.POST, instance=tag)
    
    if form.is_valid():
        form.save()
        return redirect(reverse('tag_list'))
    context['form'] = form
    return render(request, 'forms/update_tag.html', context)

def delete_post(request, slug):

    context ={}
 
    post = get_object_or_404(Post, slug = slug)
 
    if request.method =="POST":
        post.delete()
        return redirect(reverse('posts')) 
    
    return render(request, "forms/delete_post.html", context)


def delete_category(request, id):

    context ={}
 
    category = get_object_or_404(Category, id = id)
 
    if request.method =="POST":
        category.delete()
        return redirect(reverse('all_category')) 
    
    return render(request, "forms/delete_category.html", context)


def delete_tag(request, id):

    context ={}
 
    tag = get_object_or_404(Tag, id = id)
 
    if request.method =="POST":
        tag.delete()
        return redirect(reverse('tag_list')) 
    
    return render(request, "forms/delete_tag.html", context)

def create_category(request):
    context = {}
    form = CategoryForm(None or request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('all_category'))
    context['form'] = form
    return render(request, 'forms/create_category.html', context)


def create_tag(request):
    context = {}
    form = TagForm(None or request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('tag_list'))
    context['form'] = form
    return render(request, 'forms/create_tag.html', context)

@login_required(login_url='/post/login')
def dashboard(request):
    if  request.user.is_authenticated :
        user_info = CustomUser.objects.get(pk = request.user.id)
        posts = Post.objects.filter(owner__id = request.user.id).all()
        
        avatar = UserProfile.objects.filter(user__id = request.user.id).reverse()
        avatar = avatar[len(avatar) - 1] if avatar else None
    
    return render(request, 'dashboard.html', {'user_info':user_info, 'posts':posts, 'avatar':avatar})

@login_required(login_url='/post/login')
def create_post(request):
    context = {}
    form = PostForm(request.POST,request.FILES)
    if form.is_valid():
        post = form.save(commit=False)
        post.slug = slugify(post.title)
        post.owner = request.user
        post.save()
        print(post.slug)
        print('----------------------------------------------')

        return redirect(reverse('dashboard'))
    context['form'] = form
    return render(request, 'forms/create_post.html', context)



def search(request):
    context = {}
    query = request.GET.get('q', None)
    
    if query is not None:
        lookups= Q(title__icontains=query) | Q(tag__tag_name__icontains=query) | Q(bodytext__icontains=query)
        posts = Post.objects.filter(lookups).distinct()
    
    context = {'posts': posts}


    return render(request, 'search_list.html', context)

@login_required(login_url='/post/login')
def user_avatar(request):
    context = {}
    form = AvatarForm(request.POST,request.FILES)
    if form.is_valid():
        avatar = form.save(commit=False)
        avatar.user = request.user
        avatar.save()
        # return redirect('posts')
    context['form'] = form
    return render(request, 'forms/avatar.html', context)
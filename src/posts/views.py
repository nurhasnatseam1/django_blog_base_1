from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import messages
from .models import Post
from .forms import PostForm
# Create your views here.
def posts_home(request):
    queryset_list=list(Post.objects.all())
    paginator=Paginator(queryset_list,4)
    page=request.GET.get('page')
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    
    contex={
        'name':'seam',
        'obj_list':queryset,
    }
    return render(request,'posts/index.html',contex)

def posts_create(request):
    form=PostForm(request.POST or None,request.FILES or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully created new post')
            return redirect(reverse('posts:posts_home'))
    context={
        'form':form
    }
    return render(request,'posts/form.html',context)

def posts_delete(request,post_id=None):
    obj=get_object_or_404(Post,id=post_id)
    if request.method=="POST":
        obj.delete()
        return redirect(reverse('posts:posts_home'))
    return render(request,'posts/delete.html',{"obj":obj})


def posts_update(request,post_id=None):
    obj=get_object_or_404(Post,id=post_id)
    if request.method=="POST":
        form=PostForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            obj=form.save(commit=False)
            id=obj.id
            print(obj.id )
            obj.save()
            return redirect(reverse('posts:posts_detail',kwargs={'post_id':id}))
    else:
        form=PostForm(instance=obj)
    
    context={
        'form':form
    }

    return render(request,'posts/form.html',context)

def posts_detail(request,post_id=None):
    obj=get_object_or_404(Post,id=post_id)
    return render(request,'posts/detail.html',{'obj':obj})
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .forms import FormPub
from django.shortcuts import redirect

def listar_pub(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/listar_pub.html', {'posts': posts})

def detalle_pub(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_pub.html',{'post' : post})

def nueva_pub(request):
    if request.method == "POST":
        form = FormPub(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('detalle_pub', pk=post.pk)
    else:
        formulario = FormPub()
    return render(request, 'blog/nueva_pub.html', {'formulario': formulario})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = FormPub(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('detalle_pub', pk=post.pk)
    else:
        form = FormPub(instance=post)
        return render(request, 'blog/nueva_pub.html', {'formulario': form})

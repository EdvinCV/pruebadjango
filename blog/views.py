from django.shortcuts import render
from .models import Post
from django.utils import timezone

def listar_pub(request):
    pubs = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')   
    return render(request, 'blog/listar_pub.html', {'pubs': pubs})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Post, Like
from .forms import PostForm

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'posts/detail.html', {'post': post})

@login_required
def create(request):
    if request.method == 'POST':
        # Deserialize your POST data
        form = PostForm(request.POST)
        model = form.save(commit=False)

        # Create an actual model
        model.user = request.user
        model.save()

        return redirect('posts:detail', pk=model.pk)

    elif request.method == 'GET':
        form = PostForm()
        return render(request, 'posts/create.html', {'form': form})

@login_required
def like(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.likes.filter(user=request.user).exists():
        return JsonResponse({ 'error': 'you already like this post'}, status=401)
    else:
        like = Like.objects.create(user=request.user)
        post.likes.add(like)
        post.save()

        return JsonResponse({ 'success': True })

@login_required
def unlike(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = post.likes.filter(user=request.user)

    if like.exists():
        post.likes.remove(like.first())
        post.save()
        like.delete()
        return JsonResponse({ 'success': True })
    else:
        return JsonResponse({ 'error': 'you don\'t already like this post'}, status=401)
        

@login_required
def likes(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.likes.filter(user=request.user).exists():
        return JsonResponse({ 'success': True })
    else:
        return JsonResponse({ 'success': False })


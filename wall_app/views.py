from django.shortcuts import render, redirect, HttpResponse
from .models import Post, Comment
from login_app.models import User
from django.contrib import messages

# Create your views here.
def wall_index(request):
    if not 'user_id' in request.session:
        messages.error(request, "Please Login")
        return redirect('/')
    context = {
        'posts' : Post.objects.all(),
        'comments' : Comment.objects.all()
    }
    return render(request, "wall_index.html", context)

def create_post(request):
    post = Post.objects.create(
        post_message = request.POST['post_message'],
        user = User.objects.get(id=request.session['user_id'])
    )
    post.save()
    return redirect('/wall')

def create_comment(request):
    comment = Comment.objects.create(
        comment_message = request.POST['post_comment'],
        user = User.objects.get(id=request.session['user_id']),
        post = Post.objects.get(id=request.POST['post_id'])
    )
    comment.save()
    return redirect('/wall')

def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id).delete()
    return redirect('/wall')

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id).delete()
    return redirect('/wall')
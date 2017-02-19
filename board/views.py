# class Post(models.Model):
#     post_title = models.CharField(max_length=120)
#     post_pub_date = models.DateTimeField('publish date')
#     post_desc = models.TextField()
#     post_author = models.CharField(max_length=24)
#

from django.shortcuts import render
from .models import Post, Comment
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

def index(request):
    posts = Post.objects.all()
    five = posts.order_by('-post_pub_date')[:5]
    return render(request, 'board/index.html', {'posts':five})

@csrf_exempt
def delete_post(request):
    post_id = request.POST.get("post_id")
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponse("success")


@csrf_exempt
def newpost(request):
    text = request.POST.get("text")
    title = request.POST.get("title")
    author = request.POST.get("author")
    post = Post.objects.create(post_title=title,post_pub_date=timezone.now(), post_author=author, post_desc=text)
    return render(request, 'board/post.html', {'post':post})

@csrf_exempt
def newcomment(request):
    post_id = int(request.POST.get("post"))
    commenttext = request.POST.get("text")
    commentauthor = request.POST.get("author")
    comment = Comment.objects.create(comment_text=commenttext, comment_author=commentauthor, post_id=post_id)
    return render(request, 'board/comment.html', {'comment':comment})
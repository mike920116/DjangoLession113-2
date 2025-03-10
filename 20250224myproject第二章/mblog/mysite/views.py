from django.shortcuts import render, redirect
from mysite.models import Post
from datetime import datetime

def homepage(request):
    try:
        # 獲取所有貼文，並根據日期排序（最近的貼文在前）
        posts = Post.objects.all().order_by('-pub_date')  # 假設 Post 模型有 created_at 欄位
        now = datetime.now()

        # 這裡你可以加入過濾條件，譬如只顯示某些類型的貼文
        # example: posts = Post.objects.filter(status='published').order_by('-created_at')

        return render(request, "index.html", {
            'posts': posts,
            'now': now,
        })
    except Post.DoesNotExist:
        # 如果沒有貼文，顯示一個空的訊息或處理
        return render(request, "index.html", {
            'posts': [],
            'now': now,
            'error_message': 'No posts available at the moment.'  # 顯示錯誤訊息
        })
    except Exception as e:
        # 捕獲其他錯誤，並顯示
        return render(request, "index.html", {
            'error_message': f'An error occurred: {str(e)}',
            'now': now
        })
def showpost(request, slug):
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')
    
def post_list(request):
    # 假設你有一個 Post 模型來儲存貼文
    # from .models import Post
    # posts = Post.objects.all()
    posts = []  # 如果沒有 Post 模型，這裡可以先用空列表
    return render(request, 'post_list.html', {'posts': posts})

def about(request):
    return render(request, 'about.html')  # 返回一個簡單的關於我們頁面

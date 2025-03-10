from django.urls import path
from django.contrib import admin
from mysite.views import homepage, showpost, post_list, about

urlpatterns = [
    path('', homepage, name='home'),
    path('post/<slug:slug>/', showpost),
    path('post-list/', post_list, name='post_list'),  # 為貼文列表頁面定義名稱
    path('about/', about, name='about'),  # 為關於我們頁面定義名稱
    path('admin/', admin.site.urls),
]

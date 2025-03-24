from django.contrib import admin
from django.urls import path, include
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('about/', views.about),
    path('about/<int:author_no>/', views.about),
    path('list/<int:yr>/<int:mon>/<int:day>/', views.listing, name='listing-url'),
    path('post/<int:yr>/<int:mon>/<int:day>/<int:post_num>/', views.post, name='post-url'),
    path('newinfo/', include('mysite.urls')),  
]



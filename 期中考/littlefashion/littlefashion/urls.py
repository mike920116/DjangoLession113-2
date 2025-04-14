from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('faq/', TemplateView.as_view(template_name='faq.html'), name='faq'),
    path('product-detail/', TemplateView.as_view(template_name='product-detail.html'), name='product-detail'),
    path('products/', TemplateView.as_view(template_name='products.html'), name='products'),
    path('sign-in/', TemplateView.as_view(template_name='sign-in.html'), name='sign-in'),
    path('sign-up/', TemplateView.as_view(template_name='sign-up.html'), name='sign-up'),
]

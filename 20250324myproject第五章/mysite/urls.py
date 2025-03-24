from django.urls import path
from . import views  # 從同一個資料夾中匯入 views 模組

my_patterns = [
    path('company/', views.company, name='company'),
    path('sales/', views.sales, name='sales'),
    path('contact/', views.contact, name='contact'),
]

urlpatterns = my_patterns  # 確保這個變數存在

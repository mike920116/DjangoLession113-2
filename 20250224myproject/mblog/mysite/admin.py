#  Django 管理後台（Admin Site）註冊 Post 模型，並自訂其顯示方式
from django.contrib import admin
from .models import Post  # 匯入 Post 模型

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')  # 列表顯示的欄位
    search_fields = ('title',)  # 可在管理後台搜尋 title
    list_filter = ('pub_date',)  # 依照日期篩選
    prepopulated_fields = {'slug': ('title',)}  # 當輸入 title 時，自動生成 slug

admin.site.register(Post, PostAdmin)

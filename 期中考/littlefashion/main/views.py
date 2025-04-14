from django.shortcuts import render
import random

# Create your views here.

def index(request):
    # 模擬 Featured Products 和 Onsell Products 資料
    featured_products = [
        {"name": "Tree pot", "price": 25, "image": "images/product/evan-mcdougall-qnh1odlqOmk-unsplash.jpeg"},
        {"name": "Fashion set", "price": 35, "image": "images/product/jordan-nix-CkCUvwMXAac-unsplash.jpeg"},
        {"name": "Juice Drinks", "price": 45, "image": "images/product/nature-zen-3Dn1BZZv3m8-unsplash.jpeg"},
    ]

    onsell_products = [
        {"name": "Package", "price": 50, "image": "images/product/team-fredi-8HRKoay8VJE-unsplash.jpeg"},
        {"name": "Bottle", "price": 100, "image": "images/product/quokkabottles-kFc1_G1GvKA-unsplash.jpeg"},
        {"name": "Medicine", "price": 200, "image": "images/product/anis-m-WnVrO-DvxcE-unsplash.jpeg"},
    ]

    # 隨機生成描述內容
    descriptions = [
        "This product is crafted with the finest materials.",
        "A perfect choice for your daily needs.",
        "Designed to bring elegance and functionality.",
        "Highly recommended by our customers.",
        "A blend of style and comfort.",
    ]

    for product in featured_products:
        product["description"] = random.choice(descriptions)

    for product in onsell_products:
        product["description"] = random.choice(descriptions)

    context = {
        "featured_products": featured_products,
        "onsell_products": onsell_products,
    }

    return render(request, "index.html", context)

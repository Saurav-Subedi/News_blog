from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.db.models import Q
from rest_framework import  viewsets
from .new_serializer import NewsSerializer

class NewsViews(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer



# Create your views here.
def index(request):
    if request.method == 'POST':
        criteria = request.POST['criteria']
        data={
            'newsData': News.objects.filter(Q(title__icontains=criteria) |
                                             Q(description__icontains=criteria)
                                             | Q(category__name__icontains=criteria)
                                             )
        }
        return render(request,'search.html',data)
    else:
        data={
            'bannerData': News.objects.filter(is_banner=1),
            'newsData': News.objects.filter()
        }
        return render(request,'index.html',data)

def news_details(request,slug):
    obj = News.objects.get(slug=slug)
    obj.page_views += 1
    obj.save()
    data={
        'newsData': News.objects.get(slug=slug),
        'relatedNews': News.objects.all().exclude(slug=slug)
    }
    return render(request,'news.html',data)

def category_news(request,slug):
    data={
        'catData': Category.objects.get(slug=slug),
        'newsData': News.objects.filter(category__slug=slug)
    }
    return render(request,'category.html',data)
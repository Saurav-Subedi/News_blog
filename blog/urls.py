from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.NewsViews)



urlpatterns = [
    path('', views.index,name='index'),
    path('news/<slug>',views.news_details,name='news'),
    path('category/<slug>',views.category_news,name='category'),
    path('api', include(router.urls)),

]

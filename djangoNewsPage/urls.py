from django.urls import path
import djangoNewsPage.views as news_views

urlpatterns = [
    path('', news_views.news, name='news'),
]
from django.urls import path
import djangoNewsPage.views as news_views

urlpatterns = [
    path('', news_views.NewsView.as_view(), name='news'),
]
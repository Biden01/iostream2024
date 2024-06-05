from django.urls import path
import djangoLecturePage.views as lecture_views

urlpatterns = [
    path('', lecture_views.lecture, name='lecture'),
]
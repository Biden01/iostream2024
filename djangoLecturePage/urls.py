from django.urls import path
import djangoLecturePage.views as lecture_views

urlpatterns = [
    path('', lecture_views.LecturePageView.as_view(), name='lecture'),
    path('print_input/', lecture_views.PrintInputView.as_view(), name='print_input'),
]
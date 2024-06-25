from django.urls import path
import djangoLecturePage.views as lecture_views

urlpatterns = [
    path('', lecture_views.LecturePageView.as_view(), name='lecture'),
    path('print_input/', lecture_views.PrintInputView.as_view(), name='print_input'),
    path('if_else/', lecture_views.IfElseView.as_view(), name='if_else'),
    path('calculations/', lecture_views.CalculationsView.as_view(), name='calculations'),
]
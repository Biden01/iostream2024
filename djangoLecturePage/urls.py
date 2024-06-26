from django.urls import path
import djangoLecturePage.views as lecture_views

urlpatterns = [
    path('', lecture_views.LecturePageView.as_view(), name='lecture'),
    path('print_input/', lecture_views.PrintInputView.as_view(), name='print_input'),
    path('if_else/', lecture_views.IfElseView.as_view(), name='if_else'),
    path('calculations/', lecture_views.CalculationsView.as_view(), name='calculations'),
    path('forloop/', lecture_views.ForLoopView.as_view(), name='forloop'),
    path('str/', lecture_views.StrView.as_view(), name='str'),
    path('whileloop/', lecture_views.WhileLoopView.as_view(), name='whileloop'),
    path('list/', lecture_views.ListView.as_view(), name='list'),
    path('function/', lecture_views.FunctionView.as_view(), name='function'),
    path('array/', lecture_views.ArrayView.as_view(), name='array'),
    path('sets/', lecture_views.SetsView.as_view(), name='sets'),
    path('dictionary/', lecture_views.DictionaryView.as_view(), name='dict'),
]
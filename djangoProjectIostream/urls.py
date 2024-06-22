from django.contrib import admin
from django.urls import path, include
from djangoMainPage import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.HomeView.as_view(), name='main'),
    path('lecture/', include("djangoLecturePage.urls")),
    path('news/', include("djangoNewsPage.urls")),
    path('logout/', main_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('djangoUsers.urls')),
]

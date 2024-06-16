from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
import djangoMainPage.views as main_views
from djangoProjectIostream import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name='main'),
    path('lecture/', include("djangoLecturePage.urls")),
    path('news/', include("djangoNewsPage.urls")),
    path('logout/', main_views.logoutProfile, name='logout'),
    path('accounts/', include('djangoUsers.urls')),
]

from django.shortcuts import render
from django.views import View


class NewsView(View):
    def get(self, request):
        return render(request=request, template_name="news/news.html")

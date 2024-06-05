from django.shortcuts import render

# Create your views here.
def news(request):
    return render(request=request, template_name="news/news.html")
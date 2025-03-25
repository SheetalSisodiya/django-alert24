from django.shortcuts import render
from main.models import Categories,News
from .forms import Students



def search(request):
    query = request.GET.get('search')
    data = News.objects.filter(title__icontains = query)
    context = {
        'news': data
    }
    return render(request, 'search.html', context)


def studentView(request):
    sf = Students()
    return render(request, 'form.html',{'fm':sf})





def home(request):
    category = Categories.objects.all()
    allnews = News.objects.all().order_by('-id')
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'categories': category,
        'allNews': allnews,
        'topNews': topNews
        }
    return render(request, 'index.html', context )

def india(request):
    
    category = Categories.objects.all()
    indianews = News.objects.filter(category__title = 'India News').order_by('-id')
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'categories': category,
        'indiaNews': indianews,
        'topNews': topNews
        }
    return render(request,'categories/india.html',context)






def bolly(request):
    category = Categories.objects.all()
    bollynews = News.objects.filter(category__title = 'Bollywood News').order_by('-id')
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'categories': category,
        'bollyNews': bollynews,
        'topNews': topNews
        }
    return render(request, 'categories/bollywood.html', context)


def sports(request):
    category = Categories.objects.all()
    sportsnews = News.objects.filter(category__title = 'Sports news').order_by('-id')
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'categories': category,
        'sportsNews': sportsnews,
        'topNews': topNews
        }
    return render(request, 'categories/sports.html', context)


def healthy(request):
    category = Categories.objects.all()
    healthynews = News.objects.filter(category__title = 'Healthy News').order_by('-id')
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'categories': category,
        'healthyNews': healthynews,
        'topNews': topNews
        }
    return render(request, 'categories/healthy.html', context)





def details(request, id):
    category = Categories.objects.all()
    news = News.objects.get(pk = id)
    topNews = News.objects.all().order_by('-id')[:5]
    context = {
        'news': news,
        'topNews': topNews
        }
    return render(request, 'details.html', context)



    

























def about(request):
    return render(request,'about.html')
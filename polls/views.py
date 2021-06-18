from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Article, Info, Image, Subject, BestWorks



"""class IndexView(generic.ListView):
    template_name = 'polls/main_page.html'
    context_object_name = 'latest_info_list'

    def get_queryset(self):
         return Info.objects.filter(
        pub_date__lte=timezone.now(), 
    ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    ...
    def get_queryset(self):

        return Info.objects.filter(pub_date__lte=timezone.now())"""

def main_page(request):
    latest_info_list = Info.objects.all().order_by('-pub_date')
    return render(request, 'polls/main_page.html', {"latest_info_list": latest_info_list})

def inf_detail(request, info_id):
    info = Info.objects.get(pk=info_id)
    return render(request, 'polls/info_detail.html', {'info': info})

def zadan_main(request):
    latest_articles_list = Article.objects.all()
    return render(request, 'polls/zadan.html', {'latest_articles_list': latest_articles_list})

def art_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    subject = get_object_or_404(Article, pk=article_id)
    return render(request, 'polls/art_detail.html', {'article': article, 'subject': subject})

def photo_page(request):
    latest_photoes = Image.objects.all().order_by('-pub_date')
    return render(request, 'polls/photoes.html', {'latest_photoes': latest_photoes})

def inf_for(request):
    return render(request, 'polls/info.html')

def best_works(request):
    latest_works = BestWorks.objects.all().order_by('-pub_date')
    return render(request, 'polls/best.html', {'latest_works': latest_works})

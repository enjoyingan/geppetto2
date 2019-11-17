# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Market
from .forms import MarketPost
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def market(request):
    markets = Market.objects.all().order_by('-id') # 객체 묶음 가져오기
    return render(request, 'market.html', {'markets':markets })

def detail4(request, market_id) : 
    market_detail = get_object_or_404(Market, pk= market_id) # 특정 객체 가져오기(없으면 404 에러)
    return render(request, 'detail4.html', {'market':market_detail})

def delete4(request, market_id):
    market= get_object_or_404(Market, pk= market_id) # 특정 객체 가져오기(없으면 404 에러)
    market.delete()
    return redirect('market')

def marketpost(request):
    # post 방식으로 들어오면 글 생성
    if request.method=='POST':
        form=MarketPost(request.POST)
        # form 양식이 유효하면
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('market')
    
    # get 방식으로 들어오면 페이지 띄우기
    else:
        form=MarketPost()
        return render(request, 'new4.html',{'form': form})
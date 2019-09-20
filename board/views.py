from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
# Create your views here.


def notice(request):
    notice = NoticeBoard.objects.all().order_by('-id')
    return render(request, 'notice.html' , {'notices' : notice})

def notice_detail(request, notice_id):
    notice_detail = get_object_or_404(NoticeBoard , pk = notice_id)
    return render(request, 'notice_detail.html' ,{'notice_detail' : notice_detail})


def notice_post(request):
    if request.method == 'POST':
        forms = NoticeForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('notice')
    else:
        forms = NoticeForm()
    return render(request, 'notice_post.html' , {'forms' : forms})


# def notice_edit(request , )
        
    
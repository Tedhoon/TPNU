from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required



def notice(request):
    notice = NoticeBoard.objects.all().order_by('-id')
    return render(request, 'notice.html' , {'notices' : notice})

def notice_detail(request, notice_id):
    notice_detail = get_object_or_404(NoticeBoard , pk = notice_id)
    return render(request, 'notice_detail.html' ,{'notice_detail' : notice_detail})

@login_required
def notice_post(request):
    if request.method == 'POST':
        forms = NoticeForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('notice')
    else:
        forms = NoticeForm()
    return render(request, 'notice_post.html' , {'notice_form' : forms})

def notice_edit(request, notice_detail_id):
    notice_detail = get_object_or_404(NoticeBoard , pk = notice_detail_id)

    edit_notice_form = NoticeForm(instance = notice_detail)

    if request.method == 'POST':
        edit_notice_form = NoticeForm(request.POST , instance = notice_detail)
        if edit_notice_form.is_valid():
            edit_notice_form.save()
            return redirect('notice')

    return render(request, 'notice_edit.html', {'edit_notice_form' : edit_notice_form ,'notice_detail' : notice_detail} )


def notice_delete(request ,notice_detail_id):
    # if username == ~:
    notice_detail = get_object_or_404(NoticeBoard, pk = notice_detail_id)
    notice_detail.delete()
    return redirect('notice')
        
    
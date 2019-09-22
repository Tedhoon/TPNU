from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# pagination
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy






def notice(request):
    notice = NoticeBoard.objects.all().order_by('-id')

    paginator = Paginator(notice , 10) #10페이지씩 자르기
    page = request.GET.get('page')
    posts = paginator.get_page(page) #request된 페이지를 담는다

    return render(request, 'notice.html' , {'notices' : notice , 'notice_posts' : posts})





def notice_detail(request, notice_id):
    notice_detail = get_object_or_404(NoticeBoard , pk = notice_id)
    return render(request, 'notice_detail.html' ,{'notice_detail' : notice_detail})





# @login_required
# def notice_post(request):
#     if request.method == 'POST':
#         forms = NoticeForm(request.POST)
#         if forms.is_valid():
#             forms.save()
#             return redirect('notice')
#     else:
#         forms = NoticeForm()
#     return render(request, 'notice_post.html' , {'notice_form' : forms})



class NoticePost(CreateView):
     
    def get(self, request, *args, **kwargs):
        context = {'notice_form': NoticeForm()}
        return render(request, 'notice_post.html', context)

    def post(self, request, *args, **kwargs):
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.instance.author = self.request.user
            form.instance.save()
            form.save()
            
            return HttpResponseRedirect(reverse_lazy('notice'))
        return render(request, 'notice_post.html', {'notice_form': form})

# class NoticePost(CreateView):
#     form = NoticeForm()
#     template_name = 'notice_post.html'
    

    # def form_valid(self, form):
    #     form.instance.author.id = self.request.user.id
    #     if form.is_valid():
    #         form.instance.save()
    #         return redirect('/')
    #     else:
    #         return self.render_to_response({'notice_form':form})



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
        
    
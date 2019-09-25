from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView , DeleteView 
# from django.views.generic import RedirectView
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse_lazy



def image(request):
    image = ImageBoard.objects.all().order_by('-id')

    return render(request, 'image.html' , {'images' : image })



def image_detail(request, image_id):
    image_detail = get_object_or_404(ImageBoard , pk = image_id)
    return render(request, 'image_detail.html' ,{'image_detail' : image_detail})





class ImagePost(CreateView):
     
    def get(self, request, *args, **kwargs):
        context = {'image_form': ImageForm()}
        return render(request, 'image_post.html', context)

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST , request.FILES)
        if form.is_valid():
            form.instance.author = self.request.user
            form.instance.save()
            form.save()
            return HttpResponseRedirect(reverse_lazy('image'))
        return render(request, 'image_post.html', {'image_form': form})

# class PostLikeRedirect(RedirectView):
#     def get_redirect_url(self, *args , **kwargs):
#         slug = self.kwargs.get("slug") #이 안에 "pk값.. 8: 42"
        
#         obj = get_object_or_404(ImageBoard , slug=slug)
#         return obj.get_absolute_url()



def image_edit(request, image_detail_id):
    image_detail = get_object_or_404(ImageBoard , pk = image_detail_id)

    edit_image_form = ImageForm(instance = image_detail)

    if request.method == 'POST':
        edit_image_form = ImageForm(request.POST, request.FILES , instance = image_detail)
        
        if request.user != image_detail.author:
            raise Http404

        if edit_image_form.is_valid():
            edit_image_form.save()
            return redirect('image')


    return render(request, 'image_edit.html', {'edit_image_form' : edit_image_form ,'image_detail' : image_detail} )



class ImageDelete(DeleteView):

    model = ImageBoard
    success_url = reverse_lazy('image')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object() #이게 타이틀임
        self.author = self.get_object().author # 작성자 name

        if self.request.user == self.author:
            
            success_url = self.get_success_url()

            self.object.delete()
            return HttpResponseRedirect(success_url)

        else:
            raise Http404
    

# @login_required

# def post_like_toggle(request, image_id):
#     # GET파라미터로 전달된 이동할 URL
#     next_path = request.GET.get('next')
#     # image_id에 해당하는 Post객체
#     post = get_object_or_404(ImageBoard, pk=image_id)
#     # 요청한 사용자
#     user = request.user

#     # 사용자의 like_posts목록에서 like_toggle할 Post가 있는지 확인
#     filtered_like_posts = user.like_posts.filter(pk=image_id)
#     # 존재할경우, like_posts목록에서 해당 Post를 삭제
#     if filtered_like_posts.exists():
#         user.like_posts.remove(post)
#     # 없을 경우, like_posts목록에 해당 Post를 추가
#     else:
#         user.like_posts.add(post)

#     # 이동할 path가 존재할 경우 해당 위치로, 없을 경우 Post상세페이지로 이동
#     if next_path:
#         return redirect(next_path)
#     return redirect('image_detail', image_id=image_id)



# def detail(request):
#     user = request.user
    
#     # 이미 좋아요를 눌렀다면 좋아요 취소, 안 눌렀으면 좋아요 버튼이 뜨도록 한다.
#     if blog_detail.likes.filter(id = user.id): # 로그인한 user가 현재 blog 객체에 좋아요를 눌렀다면
#         message = "좋아요 취소"
#     else:
#         message = "좋아요"

#     return render(request, 'blog/detail.html', {'blog':blog_detail, 'message':message})
    
# def post_like(request, blog_id):
#     user = request.user # 로그인된 유저 객체를 가져온다.
#     blog = get_object_or_404(Blog, pk = blog_id) # 좋아요 버튼이 눌린 글을 가져온다.

#     # 이미 좋아요를 눌렀다면 좋아요 취소, 안 눌렀으면 좋아요 버튼이 뜨도록 한다.
#     if blog.likes.filter(id = user.id): # 로그인한 user가 현재 blog 객체에 좋아요를 눌렀다면
#         blog.likes.remove(user) # 해당 좋아요를 없앤다.
#     else:
#         blog.likes.add(user) # 아직 좋아요를 안 눌렀으면 좋아요를 추가한다.

#     return redirect('/blog/'+str(blog_id)) # 필요 정보들을 넘기고 detail 페이지로 넘어간다

    

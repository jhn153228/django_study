from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView

from .models import Post


# post_list = login_required(ListView.as_view(model=Post, paginate_by=10))

@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    paginate_by = 10

post_list = PostListView.as_view()

# @login_required
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q,
#     })


# def post_detail(request: HttpRequest, pk: int) -> HttpResponse: # 구글 정규식? 이었던걸로 기억함
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html', {
#         'post' : post,
#     })

# post_detail = DetailView.as_view(
#     model=Post,
#     queryset=Post.objects.filter(is_public=True))

class PostDetailView(DetailView):
    model = Post

    # queryset = Post.objects.filter(is_public=True)
    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter()
        return qs


post_detail = PostDetailView.as_view()


def archives_year(requests, year):
    return HttpResponse(f'{year}_archives!!')

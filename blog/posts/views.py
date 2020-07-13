from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator # 추가된 코드
# Create your views here.                   # 장고 내장 페이지네이션 기능을 가져온다.
def home(request):
    posts = Post.objects.all() # posts는 게시글이 담긴 배열

    paginator = Paginator(posts, 2) # 페이지네이터 함수 사용 # 추가된 코드
    page_number = request.GET.get("page") # 페이지 넘버 가져오기 # 추가된 코드
    page_posts = paginator.get_page(page_number) # 추가된 코드
    
    return render(request, "posts/index.html", {"posts":page_posts}) # 변경된 코드

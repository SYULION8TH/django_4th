from django.shortcuts import get_object_or_404, redirect, render # 추가된 코드
from .forms import BlogPost # 추가 코드 forms의 함수 호출
from .models import Post
from django.core.paginator import Paginator 
from django.utils import timezone
# Create your views here.                   # 장고 내장 페이지네이션 기능을 가져온다.
def home(request):
    posts = Post.objects.all() # posts는 게시글이 담긴 배열

    paginator = Paginator(posts, 2) # 페이지네이터 함수 사용 
    page_number = request.GET.get("page") # 페이지 넘버 가져오기 
    page_posts = paginator.get_page(page_number) 
    
    return render(request, "posts/index.html", {"posts":page_posts}) 

def detail(request, pk): # 추가된 코드
    post = get_object_or_404(Post, pk = pk)
    
    return render(request, 'posts/detail.html', {"post":post})

def blogpost(request):
    if request.method == 'POST': # 요청 메소드가 POST일 때 요즘 많이 배우니깐 난 정은이 믿어^^
        form = BlogPost(request.POST, request.FILES) # 폼에 데이터와 파일 넣기
        if form.is_valid(): # validation 유효성 검사
            post = form.save(commit=False) # post에 담기 commit이 true냐 false냐는 지금 바로 저장하냐 나중에 저장하냐 차이, 나중에 저장하면 post.save()메소드를 이용하여 저장해주어야함.
            post.create_at = timezone.now() # 만들어진 시간 넣기(아마 안넣어도 될걸)
            post.save() # 데이터 저장
            return redirect('/posts/' + str(post.id)) # 리다이렉팅 알아서 설명 넣어
    else: # POST가 아닐때
        form = BlogPost()
        return render(request, 'posts/new.html', {'form':form})


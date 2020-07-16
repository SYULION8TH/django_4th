# django_4th
장고 네번째 자료

## detail
### index.html
```html
<a href= "{% url 'detail' post.id %}">..more</a> 
```

### views.py
```python
from django.shortcuts import get_object_or_404, render

def detail(request, post_id): # 추가된 코드
    post = get_object_or_404(Post, pk = post_id)
    
    return render(request, 'posts/detail.html', {"post":post})
```
### urls.py
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts.views.home, name="home"), 
    path('posts/<int:post_id>', posts.views.detail, name='detail'), # 추가된 코드
]
```

## create(form)
### forms.py
```python
from django import forms # 장고에서 forms 모듈 import
from .models import Post # 모델에서 Post를 임포트

class BlogPost(forms.ModelForm): # 모델 폼클래스를 이용해서 Post모델로 간단히 필드 작성
    class Meta:
        model = Post # 호환될 모델 클래스
        fields = ['title', 'body', 'img'] # 작성할 Post의 필드들
```

### views.py
```python
from .forms import BlogPost
from django.shortcuts import get_object_or_404, render, redirect # 추가된 코드
```
BlogPost를 가져와 줍니다.
```python
def blogpost(request):
    if request.method == 'POST': # 요청 메소드가 POST일 때
        form = BlogPost(request.POST, request.FILES) # 폼에 데이터와 파일 넣기
        if form.is_valid(): # validation 유효성 검사
            post = form.save(commit=False) # post에 담기 commit이 true냐 false냐는 지금 바로 저장하냐 나중에 저장하냐 차이, 나중에 저장하면 post.save()메소드를 이용하여 저장해주어야함.
            post.create_at = timezone.now() # 만들어진 시간 넣기(아마 안넣어도 될걸)
            post.save() # 데이터 저장
            return redirect('/posts/' + str(post.id)) 
    else: # POST가 아닐때
        form = BlogPost()
        return render(request, 'posts/new.html', {'form':form})
```
### urls.py
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts.views.home, name="home"), 
    path('posts/<int:pk>', posts.views.detail, name='detail'), # 추가된 코드
    path('newblog/', posts.views.blogpost, name = 'newblog'), # 추가된 코드
]
```

### new.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
    integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
    integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
    crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
    integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
    crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"
    integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI"
    crossorigin="anonymous"></script>
</head>
<body>
    <div class='container'>
        <form method="POST" enctype="multipart/form-data">
            {% csrf_token %}
            <table>
                {{form.as_table}}
            </table>
            <br>
            <input class="btn btn-dart" type = "submit" value = "제출하기">
        </form>
    </div>
</body>
</html>


```

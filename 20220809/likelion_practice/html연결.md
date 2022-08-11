## 라우팅



### HTML 파일 생성

```bash
#1.어플리케이션 안에 templates 폴더 생성
#2.HTML 파일 생성(home.html)
#3.views.py에 등록

#blog/views.py
def home(request):
	return render(request, 'home.html')
	#home.html을 home 함수를 부를 때 화면에 띄우겠다.
	
#이때, 주의점
#render는 템플릿을 불러오고
#redirect는 URL로 이동함.
```



**[예시]**

blog 객체를 home.html로 넘겨주고자 할 때

```bash
#blog/views.py

from django.shorcuts import render
from .modesl import Blog #models에서 Blog 객체를 가져오기

def home(request):
	blogs = Blog.objects.all()
	#Blog의 모든 객체를 blogs에 담기
	return render(request, 'home.html', {'blogs': blogs})
	#blogs의 정보를 딕셔너리 형태로 home.html에 넘겨주기
```

-> urls.py에 등록해줘야함.

```bash
#blogproject/urls.py

from blog import views #어플리케이션의 views.py를 import

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.home, name="home")
	#views에 있는 home 함수를 메인 화면으로 연결
	#name은 home으로 지정
]
```



### HTML 파일 꾸며주기

```bash
#느낌표 + enter
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BLOG</title>
    <style>
    #body 부분을 중앙정렬 해줌.
    	body{text-align: center;}
    </style>
</head>
<body>
    <h1>Blog Page</h1>
    <br>
    #{% for blog in blogs %}...{% end for %}
    #views.py에서 전달한 blogs 데이터 리스트에서  하나씩 가져옴.
    {% for blog in blogs %}
        <h3>{{ blog.title }}</h3>
        {{ blog.writer }}
        {{ blog.pub_date }}
        {{ blog.body }}
    {% endfor %}
</body>
</html>
```



본문 내용이 많아서 더보기를 누르면 내용 보여주기

->데이터베이스를 만들어준 models.py를 수정

```bash
#blog/models.py

class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

	#body를 100자까지만 출력 하고 뒤에 ...도 같이 출력
    def summary(self):
        return self.body[:100] + "..."
```

-> 적용해주기

```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BLOG</title>
    <style>
        body{text-align: center;}
    </style>
</head>
<body>
    <h1>Blog Page</h1>
    <br>
    {% for blog in blogs %}
        <h3>{{ blog.title }}</h3>
        {{ blog.writer }}
        {{ blog.pub_date }}
        {{ blog.summary }} #blog.body를 blog.summary로 바꿔줌.
    {% endfor %}
</body>
</html>
```

->blog에 detail.html 생성해주고

->views.py에 detail.html 연결해주기

```bash
from django.shortcuts import render, get_object_or_404
#get_object_or_404 : 데이터를 받지 못하면 404 에러메시지를 띄움.
from .models import Blog

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

#detail page는 id에 맞는 것들을 들고옴.
def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    #pk는 primary key의 약자로 id값을 나타낸다.
    #id값과 일치하는 블로그의 내용을 blog에 담아준다.
    return render(request, 'detail.html', {'blog': blog})
    #그리고 이 값을 딕셔너리 형태로 detail.html로 보내준다.
```

-> urls.py에 등록해줘야함.

```bash
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    #path converter
    #객체 id가 전달되어서, page마다 url을 하나씩 꺼낼 수 있음.
    path('detail<str:id>', views.detail, name="detail")
]
```

-> detail.html 꾸미기

```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DETAIL</title>
    <style>
        body{text-align: center;} #중앙정렬
    </style>
</head>
<body>
    <h1>{{ blog.title }}</h1>
    작성자: {{ blog.writer }}
    <br> #개행
    날짜: {{ blog.pub_date }}
    <hr> #가느다란 선
    {{ blog.body }}
    <br>
    <br>
    <a href="{% url 'home' %}">Home</a>
</body>
</html>
```

-> home.html로 이동하여 detil.html을 열람할 수 있도록 해주기

```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BLOG</title>
    <style>
        body{text-align: center;}
    </style>
</head>
<body>
    <h1>Blog Page</h1>
    <br>
    {% for blog in blogs %}
        <h3>{{ blog.title }}</h3>
        {{ blog.writer }}
        {{ blog.pub_date }}
        {{ blog.summary }}
        #parameter로 blog의 id를 보내고
        #more를 클릭하면 페이지가 이동함.
        <a href="{% url 'detail' blog.id %}">more</a>
    {% endfor %}
</body>
</html>
```
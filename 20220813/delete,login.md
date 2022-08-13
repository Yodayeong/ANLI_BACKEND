## Delete



1. delete 기능을 구현할 함수 정의

   ```bash
   #blog/views.py
   def delete(request, id):
       delete_blog = Blog.objects.get(id=id)
       delete_blog.delete()
       #삭제를 했으니, home으로 redirect
       return redirect('home')
   ```

2. urls.py 수정

   ```bash
   #blogproject/urls.py
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', views.home, name="home"),
       path('detail/<str:id>', views.detail, name="detail"),
       path('new/', views.new, name="new"),
       path('create/', views.create, name="create"),
       path('edit/<str:id>', views.edit, name="edit"),
       path('update/<str:id>', views.update, name="update"),
       #delete + id 값이면 delete 함수 호출
       path('delete/<str:id>', views.delete, name="delete")
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

3. detail.html에서 delete 함수 실행되게

   ```bash
   #blog/templates/detail.html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>DETAIL</title>
       <style>
           body{text-align: center;}
       </style>
   </head>
   <body>
       <h1>{{ blog.title }}</h1>
       <br>
       작성자: {{ blog.writer }}
       날짜: {{ blog.pub_date }}
       <hr>
       <img src="{{ blog.image.url }}" alt="사진"><br>
       {{ blog.body }}
       <br>
       <br>
       <a href="{% url 'home' %}">Home</a>
       <a href="{% url 'edit' blog.id %}">Edit</a>
       <a href="{% url 'delete' blog.id %}">Delete</a>
   </body>
   </html>
   ```

   

## 회원가입/로그인

계정을 만든 사람들만 글을 쓸 수 있도록



**[앱 생성]**

1. 앱을 추가로 만들기

   - 회원 관련된 기능만 구분할 수 있도록

   ```bash
   python mange.py startapp accounts
   ```

2. settings.py에 앱 등록하기

   ```bash
   #blogproject/settings.py
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'blog',
       #accounts 앱 등록
       'accounts.apps.AccountsConfig',
   ]
   ```

3. acccounts 앱에서 구현하는 기능들만 따로 정리하는 urls.py 생성

   ```bash
   #accounts/urls.py
   from django.urls import path
   from . import views
   
   urlpatterns = [
       
   ]
   ```

4. accounts의 urls.py를 기본 urls.py에 연결

   ```bash
   #blogproject/urls.py
   from django.urls import include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', views.home, name="home"),
       path('detail/<str:id>', views.detail, name="detail"),
       path('new/', views.new, name="new"),
       path('create/', views.create, name="create"),
       path('edit/<str:id>', views.edit, name="edit"),
       path('update/<str:id>', views.update, name="update"),
       path('delete/<str:id>', views.delete, name="delete"),
       #accounts의 url을 포함
       path('accounts/', include('accounts.urls'))
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

   

**[회원가입/로그인 html]**

0. accounts용 templates 폴더 생성

1. templates 에 login.html 생성

   ```bash
   #accounts/templates/login.html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
       <meta name="viewport" content="width=ha, initial-scale=1.0">
       <title>Document</title>
   </head>
   <body>
       <h1>login</h1>
       <br>
       #input들을 form 태그로 감싸줌
       #urls의 login을 불러줌 -> login 함수 호출
       <form action="{% url 'login' %}" method="post">
       	#post 방식이기 때문에 csrf_token
           {% csrf_token %}
           <br>
           username:<input type="text" name="username" value="">
           <br>
           password:<input type="password" name="password" value="">
           <br>
           <input class="button" type="submit" value="login">
       </form>
   </body>
   </html>
   ```

2. templates에 signup.html 생성

   ```bash
   #accounts/templates/signup.html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
       <meta name="viewport" content="width=ha, initial-scale=1.0">
       <title>Document</title>
   </head>
   <body>
       <h1>signup</h1>
       <br>
       <form action="{% url 'signup' %}" method="post">
           {% csrf_toekn %}
           username:
           <br>
           <input type="text" name="username" value="">
           <br>
           password:
           <br>
           <input type="password" name="password1" value="">
           <br>
           #확인용 패스워드
           confirm password:
           <br>
           <input type="password" name="password2">
           <br>
           <input class="button" type="submit" value="signup">
       </form>
   </body>
   </html>
   ```

3. views.py에 로그인과 회원가입 함수 작성

   ```bash
   #accounts/views.py
   #생성한 html 페이지가 제대로 작동하는지 보기 위해서 임의로 작성
   def signup(request):
       return render(request, 'signup.html')
   
   def login(request):
       return render(request, 'login.html')
   ```

4. urls.py에 views에서 작성한 함수 등록

   ```bash
   #accounts/urls.py
   urlpatterns = [
       path('signup/', views.signup, name="signup"),
       path('login/', views.login, name="login"),
   ]
   ```

5. home.html에 login 페이지와 signup 페이지 연결

   ```bash
   #blog/templates/home.html
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Yoda's Blog</title>
       <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
       <style>
           body{text-align: center;}
       </style>
   </head>
   <body>
       <nav class="navbar bg-light">
           <div class="container-fluid">
           <a class="navbar-brand" href="#">
               <img src="{% static 'img/루피.png' %}" alt="루피" width="30" class="d-inline-block align-text-top">
               Blog Page
           </a>
           </div>
       </nav>
   
       <a href="{% url 'new' %}" class="btn btn-outline-success m-3">Write Blog</a>
       #login과 signup url을 버튼으로 연결
       <a href="{% url 'login' %}" class="btn btn-outline-success m-3">login</a>
       <a href="{% url 'signup' %}" class="btn btn-outline-success m-3">signup</a>
       <br>
   
       <div class="d-inline-flex">
           {% for blog in blogs %}
           <div class="card m-3" style="width: 18rem;">
               <img src="{{ blog.image.url }}" class="card-img-top" alt="사진"><br>
               <div class="card-body">
                   <h5 class="card-title">{{ blog.title }}</h5>
                   <p class="card-text">
                       {{ blog.writer }}
                       {{ blog.pub_date }}<br>
                       {{ blog.summary }}
                   </p>
                   <a href="{% url 'detail' blog.id %}" class="btn btn-primary">more</a>
               </div>
           </div>
           {% endfor %}
       </div>
   </body>
   </html>
   ```

6. views.py 수정(로그인/회원가입 구현 함수)

   ```bash
   #accounts/views.py
   
   from django.contrib.auth.models import User
   #장고에서 기본적으로 제공하는 User 모델(회원정보들을 담아줌)
   from django.contrib import auth
   #로그인 할 때, 회원정보가 일치하는 지 등을 판별하는 함수들을 포함
   from django.shortcuts import redirect
   
   #-----
   #signup 함수
   def signup(request):
       if request.method == "POST":
       #요청할 때 넘겨준 방식이 POST 방식이라면,
           if request.POST['password1'] == request.POST['password2']:
           #password1과 password2가 일치하면,
               user = User.objects.create_user(
               #User 모듈 안에 있는 create_user를 사용
               #user 변수 안에 정보들을 담아줌
                   username = request.POST['username'],
                   password = request.POST['password1']
               )
           auth.login(request, user)
           #로그인까지 해줌
           return redirect('/')
           #메인화면으로 돌아감
           
   #-----
   #login 함수
   def login(request):
       if request.method == 'POST':
       #요청할 때 넘겨준 방식이 POST 방식이라면,
           username = request.POST['username']
           password = request.POST['password']
           user = auth.authenticate(request, username = username, password = password)
           #username과 password로 구성된 user의 정보를 반환해서
           #user라는 변수에 담아줌
           if user is not None:
           #user 변수가 비어있지 않으면 -> 회원정보가 있으면
           #로그인해주고 home 페이지로 redirect
               auth.login(request, user)
               return redirect('home')
           else:
           #회원정보가 없으면
           #login 페이지에 머물러있고 
           #error 메시지를 login 페이지로 넘겨줌
               return render(request, 'login.html', {'error': 'username or password is incorrect'})
       return render(request, 'login.html')
   ```

7. login.html 수정(error 메시지)

   ```bash
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
       <meta name="viewport" content="width=ha, initial-scale=1.0">
       <title>Document</title>
   </head>
   <body>
       <h1>login</h1>
       <br>
       #error를 넘겨 받았을 때, error가 키값인 딕셔너리 출력
       {% if error %}
       {{ error }}
       {% endif %}
       <form action="{% url 'login' %}" method="post">
           {% csrf_token %}
           <br>
           username:<input type="text" name="username" value="">
           <br>
           password:<input type="password" name="password" value="">
           <br>
           <input class="button" type="submit" value="login">
       </form>
   </body>
   </html>
   ```

8. 로그아웃을 위한 함수 작성

   ```bash
   #accounts/views.py
   def logout(request):
       auth.logout(request)
       return redirect('/')
   ```

9. urls.py에 함수 등록

   ```bash
   #accounts/urls.py
   urlpatterns = [
       path('signup/', views.signup, name="signup"),
       path('login/', views.login, name="login"),
       #logout 페이지에 들어가면 logout 함수 호출
       path('logout/', views.logout, name="logout"),
   ]
   ```

10. home.html에 반영

    ```bash
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Yoda's Blog</title>
        <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
        <style>
            body{text-align: center;}
        </style>
    </head>
    <body>
        <nav class="navbar bg-light">
            <div class="container-fluid">
            <a class="navbar-brand" href="#">
                <img src="{% static 'img/루피.png' %}" alt="루피" width="30" class="d-inline-block align-text-top">
                안리
            </a>
            </div>
        </nav>
    
    <div>
        {% if user.is_authenticated %}
        #로그인이 되어 있다면, if문 안으로 들어감.
            {{ user.username }}님 환영합니다.
            <br>
            <a href="{% url 'logout' %}" class="btn btn-outline-success m-3">logout</a>
            <a href="{% url 'new' %}" class="btn btn-outline-success m-3">Write Blog</a>
        {% else %}
        #로그인이 되어 있지 않다면, else문 안으로 들어감.
            <a href="{% url 'login' %}" class="btn btn-outline-success m-3">login</a>
            <a href="{% url 'signup' %}" class="btn btn-outline-success m-3">signup</a>
        {% endif %}
        <br>
    </div>
    
        <div class="d-inline-flex">
            {% for blog in blogs %}
            <div class="card m-3" style="width: 18rem;">
                <img src="{{ blog.image.url }}" class="card-img-top" alt="사진"><br>
                <div class="card-body">
                    <h5 class="card-title">{{ blog.title }}</h5>
                    <p class="card-text">
                        {{ blog.writer }}
                        {{ blog.pub_date }}<br>
                        {{ blog.summary }}
                    </p>
                    <a href="{% url 'detail' blog.id %}" class="btn btn-primary">more</a>
                </div>
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    ```
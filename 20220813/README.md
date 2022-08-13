## Static & Media



### Static

- 정적 파일(img, css, js)
- 개발자가 준비해두는 파일
- 앱/프로젝트 단위로 저장



**[static 설정 과정]**

0. image set이 pillow 안에 있음

   ```bash
   pip install pillow
   ```

1) Static 폴더 만들기

   - css폴더, js폴더, img폴더 각각 만들기

     ```bash
     #blog/static/img
     위치에 이미지 사진 등록
     ```

2) settings.py에 등록하기

   ```bash
   #blogproject/settings.py
   import os
   
   #Static files(css, JavaScript, Image)
   STATIC_URL = 'static/'
   
   STATICFILES_DIRS = [
   	os.path.join(BASE_DIR, 'blog', 'static'),
   	#join함수 : 인자로 주어진 것들을 경로로 합해줌
   	#BASE_DIR/blog/static
   	#BASE_DIR은 manage.py가 위치한 폴더를 말함.
   ]
   
   STATIC_ROOT = os.path.join(BASE_DIR, 'static')
   ```

3) 정적파일(css, js, img) 넣기

   ```bash
   #blog/home.html
   {% load static %} #이미지를 넣으려면 load static 해줘야함.
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Yoda's Blog</title>
       <style>
           body{text-align: center;}
       </style>
   </head>
   <body>
       <h1>Blog PAGE</h1>
       #Blog Page 아래에 이미지 넣어주기
       <img src="{% static 'img/루피.png' %}" alt="루피">
       <div>
           <a href="{% url 'new' %}">Write Blog</a>
       </div>
       {% for blog in blogs %}
       <br>
       <br>
           <h2>{{ blog.title }}</h2>
           {{ blog.writer }}
           {{ blog.pub_date }}
           <br>
           {{ blog.summary }}
           <a href="{% url 'detail' blog.id %}">더보기</a>
       {% endfor %}
   </body>
   </html>
   ```

4) 여러 앱의 정적파일을 한 곳에 넣어주기

   - 실제 배포 환경에서는 이미지가 개발환경처럼 뜨지 않음

   - 그렇기에 여러 곳에 있는 정적파일들을 한 곳으로 모아줘야 함

     ```bash
     python manage.py collectstatic
     
     #STATIC_ROOT = os.path.join(BASE_DIR, 'static')
     #BASE_DIR에 static 폴더를 만들고 이미지를 모아줌
     ```

     

### Media

- 이용자가 업로드하는 파일
- 프로젝트 단위로 저장
- 서비스 이용자의 업로드 등으로 인해, fileFiled나 imageFiled 또는 앞의 두 필드 중 하나를 상속한 필드를 통해 저장하게 되는 파일
  - 물론 해당 필드에는 media 파일이 저장된 경로를 저장할 뿐, 필드에 파일이 직접 저장되는 것은 아님!
  - media 파일을 urlpattern에 추가함으로서 불러옴



**[media 설정 과정]**

1. settings.py에 등록

   ```bash
   #blogproject/settings.py
   MEDIA_URL = 'media/'
   
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
   ```

2. urls.py에 연결

   ```bash
   #blogproject/urls.py
   
   #장고의 gloabal settings
   from django.conf import settings
   from django.conf.urls.static import static
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', views.home, name="home"),
       path('detail/<str:id>', views.detail, name="detail"),
       path('new/', views.new, name="new"),
       path('create/', views.create, name="create"),
       path('edit/<str:id>', views.edit, name="edit"),
       path('update/<str:id>', views.update, name="update"),
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   #media 연결해주기
   ```

3. media를 저장할 수 있도록 models 수정

   ```bash
   #blog/models.py
   class Blog(models.Model):
       title = models.CharField(max_length=200)
       writer = models.CharField(max_length=100)
       pub_date = models.DateTimeField()
       #Blog 객체에 image 받는 영역 추가
       #upload_to : 저장되는 경로
       #=> MEDIA_ROOT/blog/이미지이름.확장자
       #blank=True, null=True : 빈 값이어도 된다.
       image = models.ImageField(upload_to="blog/", blank=True, null=True)
       body = models.TextField()
   
       def __str__(self):
           return self.title
       
       def summary(self):
           return self.body[:50] + '...'
   ```

4. views도 수정

   ```bash
   #blog/views.py
   def create(request):
       new_blog = Blog()
       new_blog.title=request.POST['title']
       new_blog.writer=request.POST['writer']
       new_blog.pub_date=timezone.now()
       #new_blog 객체의 image에 저장
       new_blog.image=request.FILES['image']
       new_blog.body=request.POST['body']
       new_blog.save()
       return redirect('detail', new_blog.id)
   ```

5. 데이터베이스 정리

   - 모델 변경 -> DB 충돌 가능성 있음

     - migrations 폴더 안의 migration 정보 삭제!

       => 0001, 0002, 0003 .. 으로 시작하는 파일 다 삭제

     - db.sqlite3 파일 삭제

       => 서버 구동 중이라면 꼭 멈추고 삭제

     - python manage.py makemigrations

     - python manage.py migrate

     - python manage.py createsuperuser

6. DB에 맞게 html 수정

   - new.html

     ```bash
     #blog/templates/new.html
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta http-equiv="X-UA-Compatible" content="IE=edge">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>BLOG</title>
     </head>
     <body>
         <h1>Write Your Blog</h1>
         <form action="{% url 'create' %}" method="post" enctype="multipart/form-data">
         #파일을 첨부하는 것이 있으면, enctype을 추가해주어야함.
             {% csrf_token %}
             제목:<input type="text" name="title"><br>
             작성자:<input type="text" name="writer"><br>
             #input 태그로 사진 출력
             사진:<input type="file" name="image"><br>
             본문<textarea name="body" id="" cols="30" rows="10"></textarea><br>
             <button type="submit">submit</button>
         </form>
     </body>
     </html>
     ```

   - detail.html

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
         #넘겨받은 blog 리스트의 image로 연결
         <img src="{{ blog.image.url }}" alt="사진">
         {{ blog.body }}
         <br>
         <br>
         <a href="{% url 'home' %}">Home</a>
         <a href="{% url 'edit' blog.id %}">Edit</a>
     </body>
     </html>
     ```

   - home.html

     ```bash
     {% load static %}
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta http-equiv="X-UA-Compatible" content="IE=edge">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Yoda's Blog</title>
         <style>
             body{text-align: center;}
         </style>
     </head>
     <body>
         <h1>Blog PAGE</h1>
         <img src="{% static 'img/루피.png' %}" alt="루피">
         <div>
             <a href="{% url 'new' %}">Write Blog</a>
         </div>
         <br>
         {% for blog in blogs %}
             <h3>{{ blog.title }}</h3>
             {{ blog.writer }}
             {{ blog.pub_date }}
             #넘겨받은 blog리스트의 imgage url로 이동
             <img src="{{ blog.image.url }}" alt="사진">
             {{ blog.summary }}
             <a href="{% url 'detail' blog.id %}">더보기</a>
         {% endfor %}
     </body>
     </html>
     ```



## BootStrap으로 블로그 꾸미기



0. 부트스트랩 폴더의 css, jss 폴더를 static 폴더 안으로 

1. https://getbootstrap.com/으로 접속

   

   **[card 부분]**

   - Componenets - Card

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
         #글씨체는 bootstrap.min.css로 적용
         <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
         <style>
             body{text-align: center;}
         </style>
     </head>
     <body>
         <h1>Blog PAGE</h1>
         <img src="{% static 'img/루피.png' %}" alt="루피">
         <div>
             <a href="{% url 'new' %}">Write Blog</a>
         </div>
         <br>
         {% for blog in blogs %}
         #bootstrap 가이드에 따라 card 만들어주기
         <div class="card" style="width: 18rem;">
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
     </body>
     </html>
     ```

   - Utilities - Flex

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
         <h1>Blog PAGE</h1>
         <img src="{% static 'img/루피.png' %}" alt="루피">
         <div>
             <a href="{% url 'new' %}">Write Blog</a>
         </div>
         <br>
         #d-inline-flex로 for문 전체 감싸기
         <div class="d-inline-flex">
             {% for blog in blogs %}
             #카드 사이 margin을 3만큼 주기
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

   

   **[nav바 부분]**

   - Componenets - Navbar

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
     	#아래 있던 'Blog Page' 부분과 루피 이미지 부분을 navbar로
         <nav class="navbar bg-light">
             <div class="container-fluid">
             <a class="navbar-brand" href="#">
                 <img src="{% static 'img/루피.png' %}" alt="루피" width="30" height="24" class="d-inline-block align-text-top">
                 Blog Page
             </a>
             </div>
         </nav>
     
         <div>
             <a href="{% url 'new' %}">Write Blog</a>
         </div>
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

   [button 부분]

   - Write Blog를 버튼으로

   - Componenets - Buttons

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
     
     	#div가 필요 없어서 없애고 class로 버튼 주기. margin도 3.
         <a href="{% url 'new' %}" class="btn btn-outline-success m-3">Write Blog</a>
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
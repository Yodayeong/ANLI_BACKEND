## Django Shell

- django interactive shell
  - 사용자가 명령어를 입력할 때마다 결과를 바로바로 보여줌
  - 프로젝트 파일 내의 settings.py를 기반으로 열림

```bash
python manage.py shell
```



### Django Shell 기본 명령어

- 데이터 가져오기 : Blog.objects.all()

  ```bash
  >>> from blog.models import Blog #우리가 사용한 Blog 객체 불러오기
  >>> blogs = Blog.objects.all()
  >>> blogs
  #<QuerySet [<Blog: 하이>, <Blog: 헬로>, <Blog: 경북대학교 기사>]>
  ```

  

- 특정 데이터만 가져오기 : Blog.objects.get()

  ```bash
  >>>blog = Blog.objects.get(id=1) #id가 1인 블로그 객체 가져오기
  >>> blog
  #<Blog: 하이>
  
  >>> blog.title
  #'하이'
  
  >>> blog.writer
  #'요다'
  
  >>>blog.body
  #'안녕하니'
  
  >>> from django.shortcuts import get_object_or_404
  >>> id=1000
  >>> blog = get_object_or_404(Blog, pk=id)
  #error가 뜸 (1000번째의 글이 없기 때문에)
  >>> id=1
  >>> blog
  #<Blog: 하이> (id가 1인 블로그 객체 불러옴)
  ```

  

- 특정 데이터들만 가져오기 : Blog.objects.filter()

  ```bash
  >>> blogs = Blog.objects.filter(writer='요다')
  #작성자가 요다 인 Blog 객체들을 가져온다.
  >>> blogs
  #<QuerySet [<Blog: 하이>, <Blog: 헬로>, <Blog: 경북대학교 기사>]>
  ```

  

- 데이터 생성하기 : Blog.objects.create()

  ```bash
  >>> from django.utils import timezone
  #장고에서 기본적으로 제공하는 기능 -> 현재 시간을 알 수 있음
  >>> Blog.objects.create(title='test', writer='요다영', pub_date=timezone.now(), body='testtest')
  #<Blog: test>
  #새로운 Blog 객체가 생성됨
  
  #새로운 객체를 만들어서 새로운 Blog 객체 만들기
  >>> new_blog = Blog()
  >>> new_blog.title='새로운 글'
  >>> new_blog.writer='요다영'
  >>> new_blog.pub_date=timezone.now()
  >>> new_blog.body='안녕하세요'
  >>> new_blog.save() #저장해줘야 함!!
  >>> new_blog
  #<Blog: 새로운 글>
  #새로운 Blog 객체가 생성됨
  ```

- 데이터 삭제 : delete()

  ```bash
  #get 함수를 활용한 delete
  >>> delete_blog = Blog.objects.get(id=2)
  >>> delete_blog
  #<Blog: 헬로> (삭제 할 블로그)
  >>>delete_blog.delete()
  #(1, {'blog.Blog': 1}) 
  #1개의 블로그 객체 삭제
  
  #filter 함수를 활용한 delete
  >>> delete_blog = Blog.objects.filter(writer='요다')
  >>> delete_blog.delete()
  #(2, {'blog.Blog': 2}) 
  #2개의 블로그 객체 삭제
  ```

  

- 데이터 저장 : save()

### 

## Create

new.html로 부터 새로운 정보를 받아와서 새로운 객체를 생성



1. new.html 파일 생성

   ```bash
   #templates/new.html
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
       <form action=""> #form 태그로 감싸주기
       제목:<input type="text" name="title"><br>
       작성자:<input type="text" name="writer"><br>
       본문<textarea name="body" id="" cols="30" rows="10"></textarea><br>
       <button type="submit">submit</button>
       </form>
   </body>
   </html>
   ```

2. views.py에 등록해주기

   ```bash
   #blog/views.py
   def new(request)
   	return render(request, 'new.html')
   ```

3. urls.py에 연결해주기

   ```bash
   #blogproject/urls.py
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', views.home, name="home"),
       path('detail/<str:id>', views.detail, name="detail"),
       #new/페이지로 접속하면 views.py의 new 실행
       path('new/', views.new, name="new"),
   ]
   ```

4. home.html에 new.html로 연결하는 링크 달아주기

   ```bash
   #templates/home.html
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
       ##'Write Blog'를 누르면, new.html로 연결해주기
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

5. new.html로 받아온 정보를 create 함수로 전달

   - urls.py에 create 등록

     ```bash
     #blogproject/urls.py
     urlpatterns = [
         path('admin/', admin.site.urls),
         path('', views.home, name="home"),
         path('detail/<str:id>', views.detail, name="detail"),
         path('new/', views.new, name="new"),
         #create로 접속하면 create 함수 실행
         path('create/', views.create, name="create"),
     ]
     ```

   - new.html을 create로 연결

     ```bash
     #templates/new.html
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
         #new.html을 create로 연결하는데, post방식으로 연결
         <form action="{% url 'create' %}" method="post">
         제목:<input type="text" name="title"><br>
         작성자:<input type="text" name="writer"><br>
         본문<textarea name="body" id="" cols="30" rows="10"></textarea><br>
         <button type="submit">submit</button>
         </form>
     </body>
     </html>
     ```

   - create 함수 정의

     ```bash
     #blog/views.py
     from django.shrotcuts import redirect
     from django.utils import timezone
     
     def create(request):
     	new_blog = Blog()
     	new_blog.title = request.POST['title']
     	new_blog.writer = request.POST['writer']
     	new_blog.pub_date = timezone.now()
     	new_blog.body = request.POST['body']
     	new_blog.save()
     	#detail url로 이동
     	return redirect('detail', new_blog.id)
     ```

     ***render와 redirect의 차이점**

     - render : template으로 이동 

       => 단순히 template을 보여줘야 할 때

     - redirect : url로 이동 -> url과 연결된 view가 실행 

       => POST 등의 요청을 보냈을 때 사용

6. csrf_token 사용

   - POST 양식을 사용한다면?

     => {% csrf_token %}을 사용!

     ```bash
     #blog/views.py
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
         <form action="{% url 'create' %}" method="post">
         #<form></form>태그 안에 {% csrf_token %} 적어주기!
             {% csrf_token %}
             제목:<input type="text" name="title"><br>
             작성자:<input type="text" name="writer"><br>
             본문<textarea name="body" id="" cols="30" rows="10"></textarea><br>
             <button type="submit">submit</button>
         </form>
     </body>
     </html>
     
     ```



## Update



1. edit.html 파일 생성

   ```bash
   #new.html과 동일
   #templates/edit.html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>BLOG</title>
   </head>
   <body>
   	#제목을 'Edit Your Blog'로 수정
       <h1>Edit Your Blog</h1>
       #create로 이동하지 않으므로 action 부분 삭제
       <form action="" method="post">
           {% csrf_token %}
           제목:<input type="text" name="title"><br>
           작성자:<input type="text" name="writer"><br>
           본문<textarea name="body" id="" cols="30" rows="10"></textarea><br>
           <button type="submit">submit</button>
       </form>
   </body>
   </html>
   ```

2. views.py에 edit 함수 정의

   ```bash
   #blog/views.py
   def edit(request, id):
   	edit_blog = Blog.objects.get(id=id)
   	return render(request, 'edit.html', {'blog': edit_blog})
   ```

3. urls.py에 edit 함수 연결

   ```bash
   #blogproject/urls.py
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', views.home, name="home"),
       path('detail/<str:id>', views.detail, name="detail"),
       path('new/', views.new, name="new"),
       path('create/', views.create, name="create"),
       #edit + id 페이지로 연결
       path('edit/<str:id>', views.edit, name="edit"),
   ]
   ```

4. detail.html에 edit 페이지로 연결하는 링크 추가

   ```bash
   #templates/detail.html
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
       {{ blog.body }}
       <br>
       <br>
       <a href="{% url 'home' %}">Home</a>
       #detail.html에 edit페이지를 연결해준다. 
       #연결해주면서 blog의 id 값도 넘겨준다.
       <a href="{% url 'edit' blog.id %}">Edit</a>
   </body>
   </html>
   ```

5. edit 하려면, 기존의 detail 페이지가 나와야 함

   ```bash
   #blog/edit.html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>BLOG</title>
   </head>
   <body>
       <h1>Edit Your Blog</h1>
       <form action="" method="post">
           {% csrf_token %}
           #value 값으로 기존의 detail 페이지 출력
           제목:<input type="text" name="title" value="{{blog.title}}"><br>
           작성자:<input type="text" name="writer" value="{{blog.writer}}"><br>
           #textarea는 사이에 입력
           본문<textarea name="body" id="" cols="30" rows="10">{{blog.body}}</textarea><br>
           <button type="submit">submit</button>
       </form>
   </body>
   </html>
   ```

6. 수정을 완료하고 submit을 누르면 data가 update로 이동

   - update 함수 생성

     ```bash
     #blog/views.py
     def update(request, id):
     	#특정 id 값의 Blog 객체를 update_blog에 저장
         update_blog = Blog.objects.get(id=id)
         update_blog.title=request.POST['title']
         update_blog.writer=request.POST['writer']
         update_blog.pub_date=timezone.now()
         update_blog.body=request.POST['body']
         update_blog.save()
         #detail페이지에 update_blog의 id값을 전달해줌
         return redirect('detail', update_blog.id)
     ```

   - urls.py에 update 함수 연결

     ```bash
     #blogproject/urls.py
     urlpatterns = [
         path('admin/', admin.site.urls),
         path('', views.home, name="home"),
         path('detail/<str:id>', views.detail, name="detail"),
         path('new/', views.new, name="new"),
         path('create/', views.create, name="create"),
         path('edit/<str:id>', views.edit, name="edit"),
         #update + id 페이지로 이동하면 update 함수 실행
         path('update/<str:id>', views.update, name="update"),
     ]
     ```

   - edit.html에서 submit 해주었을 때, 값을 update 함수로 전달

     ```bash
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta http-equiv="X-UA-Compatible" content="IE=edge">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>BLOG</title>
     </head>
     <body>
         <h1>Edit Your Blog</h1>
         #submit 했을 때, update 함수로 연결
         #blog의 id도 함께 전달
         <form action="{% url 'update' blog.id %}" method="post">
             {% csrf_token %}
             제목:<input type="text" name="title" value="{{blog.title}}"><br>
             작성자:<input type="text" name="writer" value="{{blog.writer}}"><br>
             본문<textarea name="body" id="" cols="30" rows="10">{{blog.body}}</textarea><br>
             <button type="submit">submit</button>
         </form>
     </body>
     </html>
     ```

     
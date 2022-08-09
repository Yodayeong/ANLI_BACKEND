### 가상 환경 설정

1. 가상 환경 만들기

   ```bash
   python -m venv myvenv
   ```

2. 가상 환경 실행

   ```bash
   source myvenv/Scripts/activate
   ```



### 장고 설치하기

1. 장고 설치하기

   ```bash
   pip install django
   ```

2. 장고 프로젝트 생성 및 해당 프로젝트로 이동

   ```bash
   #django-admin startproject <프로젝트명>
   #cd <프로젝트명>
   
   django-admin startproject blogproject
   cd blogproject
   ```

   

## models.py

: 어플리케이션의 모델(models) 파일

 => 데이터베이스를 만드는 곳



### 장고 어플리케이션 생성

1. 장고 어플리케이션 생성

   ```bash
   #python manage.py startapp <앱이름>
   
   python manage.py startapp blog
   ```

2. 장고 프로젝트에 새로 생성한 어플리케이션 등록

   ```bash
   #blogproject/settings.py
   #INSTALLED_APPS에 새로 생성한 어플리케이션 등록
   
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'blog',	#blog 어플리케이션 추가
   ]
   ```

   

### 모델(models) 생성하기

1. 블로그 사이트를 개발하기 위해 필요한 모델(models)을 생성

```bash
#blog/models.py

class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
```



### 모델(models)을 이용하여 테이블 생성

1. 마이그레이션 파일 생성

   : 우리가 만든 모델로부터 데이터베이스 테이블을 생성하기 위한 마이그레이션 파일을 생성

   ```bash
   #python manage.py makemigrations <앱이름>
   
   python manage.py makemigrations blog
   ```

2. 테이블 생성

   : 모델로부터 생성한 마이그레이션 파일을 이용하여 데이터베이스의 테이블을 생성

   ```bash
   #python manage.py migrate <앱이름>
   
   python manage.py migrate blog
   ```

   
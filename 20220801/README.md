# Django **(2022/0801)**



## Web Framework

- 웹을 만드는 작업 중에 많은 부분이 공통적이다.

- 어떤 사이트들을 만들더라도 똑같은 작업이다.

- 이런 부분들을 미리 해둔 소프트웨어를 Web Framework라고 함.

- 공통적인 작업은 Web Framework에게 맡기고, 우리는 우리 웹만의 개성을 살리자.



## MTV 패턴

: Model + Template + View



## 장고 설치

```bash
python -m pip install django
#장고가 설치 되어 있지 않으면 해준다.
django-admin startproject <프로젝트명> . 
#<프로젝트명>의 폴더로 새로운 프로젝트를 시작하겠다.
#.은 현재 폴더에서 진행하겠다.
python manage.py runserver
#runserver : 장고 기본 서버가 실행.
ctrl + C 
#server 실행이 멈춤.
```

- settings.py
  - project를 운영하는 데 필요한 여러가지 설정들이 들어가 있음.
- urls.py
  - 사용자가 접속하는 path에 따라 그 요청을 누가, 어떻게 처리할 지.
  - 라우팅과 관련됨.
- manage.py
  - project를 진행하는 데 있어서 필요한 여러가지 기능이 들어가 있는 유틸리티 파일.

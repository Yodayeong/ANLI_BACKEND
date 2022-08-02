"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#http://127.0.0.1/ #사용자가 접속할 때, 어떤 경로도 없음 => 홈
#https://127.0.0.1/app/ 

#http://127.0.0.1/create/ #사용자가 create로 접속했을 때
#https://127.0.0.1/read/1/ #사용자가 read/1/으로 접속했을 때

#urlpatters라는 리스트에는 라우팅과 관련된 정보가 적힌다.
urlpatterns = [
    path('admin/', admin.site.urls), #장고가 기본적으로 가지고 있는 관리자 화면으로 이동하기 위한 라우팅 설정
    path('', include('myapp.urls')) #사용자가 http://127.0.0.1/로 접속했을 때,(admin이 아니라 다른 경로로 접속) myapp에 있는 views로 위임
]

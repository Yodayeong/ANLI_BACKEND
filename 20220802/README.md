# Django **(2022/0801)**



## 전제적인 흐름

![KakaoTalk_20220802_234045988](Django (20220802).assets/KakaoTalk_20220802_234045988.jpg)



## app 만들기

```bash
django-admin startapp myapp
```



## Routing

- rout : 경로
- rounting : 사용자가 접속한 각각의 경로를 누가 처리할 지 지정해주는 것



[myproject - urls.py]

![1](Django (20220802).assets/1.PNG)

[myapp - urls.py]

![2](Django (20220802).assets/2.PNG)

[myapp - views.py]

![3](Django (20220802).assets/3.PNG)



**=>** myproject - urls.py  **->**  myapp - urls.py  **->**  myapp - views.py  **->**  def

# Django **(2022/0804)**



## 장고를 쓰는 이유

**(Web Server)**

: 필요로 하는 페이지를 미리 만들어 놓아야 한다.

=> static

=> 성능이 굉장히 빠름 

ex) 1.html /  2.html / 3.html ...



**(Web Application Server)**

: 웹 페이지를 생성하는 공장/ 프로그램을 하나만 만들어 놓으면 된다.

=> dynamic

=> Web Server에 비해 느림 

=> 유지, 보수가 쉬움 / 개인화된 정보를 만들어줄 수 있음

ex) view.py



## CRUD

- **C**reate / **R**ead / **U**pdate / **D**elete



### Read

1. <u>**홈페이지**</u>

​	**homepage**

​	/

​	**[myapp -> views.py]**

- ![1](Django (20220804-20220805).assets/1-16596237929382.PNG)
- ![2](Django (20220804-20220805).assets/2.PNG)



2. **<u>상세보기</u>**

​	**article**

​	/read/<id>/

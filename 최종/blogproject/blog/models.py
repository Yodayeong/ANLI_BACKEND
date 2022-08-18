from django.db import models

class Blog(models.Model): #장고에서 제공하는 models.Model를 상속받아야한다.
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    title = models.CharField(max_length=64,verbose_name = '제목')
    price = models.CharField(max_length=64,verbose_name = '가격')
    select_home = models.CharField(max_length=64,verbose_name = '집유형')
    location = models.CharField(max_length=200,verbose_name = '위치')
    smaller_period = models.CharField(max_length=64,verbose_name = '최소기간')
    startDay = models.CharField(max_length=64,verbose_name = '시작일')
    lastDay = models.CharField(max_length=64,verbose_name = '종료일')
    floor_space = models.CharField(max_length=64,verbose_name = '평수')
    bathroom = models.CharField(max_length=64,verbose_name = '욕실수')
    room = models.CharField(max_length=64,verbose_name = '방수')
    bed = models.CharField(max_length=64,verbose_name = '침대수')
    basic_info = models.CharField(max_length=64,verbose_name = '기본정보')
    option = models.CharField(max_length=64,verbose_name = '옵션')
    description = models.CharField(max_length=500,verbose_name = '설명')
    
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간') 
    #저장되는 시점의 시간을 자동으로 삽입해준다.


    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table = 'host_home'

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:50] + '...'
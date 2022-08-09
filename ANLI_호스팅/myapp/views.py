from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

#내가 해야하는거
#html - href 연결하기
#https://youtu.be/JL_uVnvk_S8

new_id = 2
topics = [
    {'id': 1, 'type': '원룸', 'title': '대구 달서구 집', 'body': '저희 집은요..'}
]

def HTMLTemplate():
    global topics
    ol = ''
    for topic in topics:
        ol += f'''<li><a href = "/read/{topic["id"]}">{topic["title"]}</a></li>'''
    return HttpResponse(f'''
    <h1>검색결과</h1>
    <ul>
        {ol}
    </ul>
    ''')

def home(request):
    article = '<a href = "/select/">Hosting</a>'
    return HttpResponse(article)

@csrf_exempt
def select(request):
    global new_id
    if request.method == 'GET':
        article = '''
        <form action = "/select/" method = "post">
            <h3>호스팅할 숙소 이름을 알려주세요.<h3>
                <p><textarea cols = "70" rows = "2" name = "title"></textarea></p>
            <h3>호스팅할 숙소 유형을 알려주세요.</h3>
            <ul>
                <li><button>원룸</button></li>
                <li><button>아파트</button></li>
                <li><button>주택</button></li>
                <li><button>오피스텔</button></li>
                <li><input name = "type" placeholder = '직접 입력하기'></li>
            </ul>
            <h3>숙소에 대해 강조하고 싶은 점이나, 장점 등을 설명해 주세요.</h3>
                <p><textarea cols = "70" rows = "10" name = "body" placeholder = "숙소를 호스팅 하게 된 이유에 대해 간략히 적어주는 것도 좋아요."></textarea></p>
                <p><input type = "submit"></p>
        </form>
        '''
        return HttpResponse(article)
    elif request.method == 'POST':
        type = request.POST['type']
        title = request.POST['title']
        body = request.POST['body']
        topics.append({'id': new_id, 'type': type, 'title': title, 'body': body})
        url = '/house_list/'
        new_id += 1
        return redirect(url)

def house_list(request):
    return HttpResponse(HTMLTemplate())

def create(request):
    article = f'''
    <form action = "/houselist/" method = "post">
        <p><textarea name = 'body' placeholder = '내용을 적어주세요!'></textarea></p>
    </form>
    '''
    return HttpResponse(article)

def read(request, id):
    global topics
    for topic in topics:
        if topic["id"] == int(id):
            article = f'''
            <h2>{topic["title"]}</h2>
            {topic["type"]}
            {topic["body"]}
            '''
    return HttpResponse(article)
